from flask import Flask, render_template, request, url_for, redirect
from script_gen import generate_script_mock, generate_script
from clips_gen import source_clips_pexley, get_scene_clips
from script_parser import parse_script
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import firestore, initialize_app, credentials, auth

app = Flask(__name__)

load_dotenv()
script_test = os.getenv("script_test")

cred = credentials.Certificate("rapidshorts-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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
    return render_template('script.html', scripttxt=generated_script)


@app.route("/clips", methods=["POST"])
def clips():
    scripttext = request.form['scripttext']
    parsed_script = parse_script(scripttext)
    print(parsed_script)
    
    test_keywords = ['lions', 'nature', 'family']
    scene_clips = get_scene_clips(test_keywords)        
    
    return render_template('clips.html', sceneclips = scene_clips)


app.run(host="0.0.0.0", port=80, debug=True)
