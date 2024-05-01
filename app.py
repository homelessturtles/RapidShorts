from flask import Flask, render_template, request, url_for, redirect, session
from script_gen import generate_script_mock, generate_script
from clips_gen import source_clips_pexley, get_scene_clips
from script_parser import parse_script
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


@app.route("/script", methods=["POST"])
def script():
    prompttxt = request.form['prompttxt']
    if (script_test == "mock"):
        print('mock function called')
        generated_script = generate_script_mock(prompttxt)
    if (script_test == "real"):
        print('real function called')
        generated_script = generate_script(prompttxt)
    user_id = 'test_user'
    file_ref = db.collection('files').document('test_document')

    file_ref.set({
        'user_id': user_id,
        'script': generated_script
    })

    return render_template('script.html', scripttxt=generated_script)


@app.route("/clips", methods=["POST"])
def clips():
    scripttext = request.form['scripttext']
    parsed_script = parse_script(scripttext)
    print(parsed_script)
    count = 0

    test_keywords = ['lions', 'nature', 'family']
    scene_clips = get_scene_clips(test_keywords)

    for k, v in scene_clips.items():
        print(f'scene links for {k}...')
        curr_scene = f'scene_{count}'
        scene_clip_links = []
        for scene in scene_clips[k]:
            doc_ref = db.collection('files').document('test_document')
            scene_clip_links.append(scene['vid_link'])
        print(scene_clip_links)
        new_element = {curr_scene: scene_clip_links}
        doc_ref.update(new_element)
        count += 1

    return render_template('clips.html', sceneclips=scene_clips)


@app.route("/edit", methods=["POST"])
def edit():
    return render_template('edit.html')


app.run(host="0.0.0.0", port=80, debug=True)
