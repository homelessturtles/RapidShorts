from flask import Flask, render_template, request, url_for, redirect, session
from script_gen import generate_script_mock, generate_script, parse_script
from clips_gen import source_clips_pexley, get_scene_clips, download_video
from voice_gen import create_speech_buffer
from vid_edit import edit_clips
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import firestore, initialize_app, credentials, auth, storage
from io import BytesIO
import tempfile
import datetime


app = Flask(__name__)


load_dotenv()
script_test = os.getenv("script_test")


cred = credentials.Certificate("rapidshorts-firebase.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'rapidshorts-b27d3.appspot.com'
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
    scenes = parse_script(generate_script(prompttxt))
    print(f'scenes...\n{scenes}')
    scenes_dict = create_dict(scenes)
    print(f'format for passing into our vid edit algo...\n{scenes_dict}')
    gen_final_vid(scenes_dict)
    final_vid_url = get_final_url()
    print(final_vid_url)
    return render_template('edit.html', video_url=final_vid_url)


def create_dict(scenes):
    '''generate proper format for video editing using parsed script and video urls'''
    keywords = []
    narration_file_names = []
    scenes_dict = {}

    # create speech files, store audio file in db, and store references to audio in dict for editing
    i = 0
    for scene in scenes.values():
        keywords.append(scene['keywords'])
        audio_fname = f'scene{i}.mp3'
        audio_clip = create_speech_buffer(scene['narration'])
        narration_file_names.append(audio_clip)
        i += 1

    # store clips urls and audio buffers for each scene into dict
    j = 0
    vid_num = 1
    clips = get_scene_clips(keywords)
    for query in clips.values():
        item = {f'scene{j}': {
            'clips': [],
            'narration': narration_file_names[j]
        }}
        for clip in query:
            item[f'scene{j}']['clips'].append(clip['vid_link'])
            vid_num += 1
        scenes_dict.update(item)
        j += 1

    return scenes_dict


def gen_final_vid(scenes_dict):
    '''generate final video using all data and upload video to firebase storage'''
    final_vid = edit_clips(scenes_dict)

    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
        temp_file_path = temp_file.name

    # Write the video data to the temporary file
    final_vid.write_videofile(temp_file_path, codec='libx264')

    blob = bucket.blob("final_video.mp4")
    with open(temp_file_path, 'rb') as f:
        blob.upload_from_file(f, content_type='video/mp4')

    temp_file.close()


def get_final_url():
    blob = bucket.blob("final_video.mp4")
    url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=15),
        # Allow GET requests using this URL.
        method="GET",
    )
    return url


app.run(host="0.0.0.0", port=80, debug=True)
