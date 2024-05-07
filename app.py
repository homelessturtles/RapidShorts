from flask import Flask, render_template, request, url_for, redirect, session
from script_gen import generate_script_mock, generate_script, parse_script
from clips_gen import source_clips_pexley, get_scene_clips, download_video
from voice_gen import create_speech_file
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import firestore, initialize_app, credentials, auth, storage


app = Flask(__name__)


load_dotenv()
script_test = os.getenv("script_test")


cred = credentials.Certificate("rapidshorts-firebase.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://rapidshorts-b27d3.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()

firebase_auth = auth


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/genvid", methods=["POST"])
def genvid():
    prompttxt = request.form['prompttxt']

    scenes_dict = {
        
    }

    keywords = []
    narration_file_names = []

    script = generate_script(prompttxt)
    scenes = parse_script(script)
    print(scenes)

    i=0
    for scene in scenes.values():
        keywords.append(scene['keywords'])
        create_speech_file(scene['narration'], f'scene{i}')
        narration_file_names.append(f'scene{i}.mp3')
        i+=1

    j=0
    vid_num = 1
    clips = get_scene_clips(keywords)
    for query in clips.values():
        item = {f'scene{j}': {
            'clips': [],
            'narration': narration_file_names[j]
        }}
        for clip in query:
            save_path = f'{vid_num}.mp4'
            url = clip['vid_link']
            download_video(url=url, save_path=save_path)
            item[f'scene{j}']['clips'].append(save_path)
            vid_num+=1
        scenes_dict.update(item)
        j+=1

    user_id = 'test_user'
    file_ref = db.collection('files').document('test_document')

    file_ref.set({
        'user_id': user_id,
        'script': script,
        'narr_file_names': narration_file_names,
    })

    return render_template('script.html')


def create_dict(clips, narration_file_names):
    scenes_dict = {}

    j=0
    for query in clips.values():
        item = {f'scene{j}': {
            'clips': [],
            'narration': narration_file_names[j]
        }}
        for clip in query:
            save_path = f'{vid_num}.mp4'
            url = clip['vid_link']
            download_video(url=url, save_path=save_path)
            item[f'scene{j}']['clips'].append(save_path)
            vid_num+=1
        scenes_dict.update(item)
        j+=1
    
    return scenes_dict


app.run(host="0.0.0.0", port=80, debug=True)
