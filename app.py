from flask import Flask, render_template, request, url_for, redirect
from script_gen import generate_script_mock, generate_script
from clips_gen import source_clips_pexley
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
script_test = os.getenv("script_test")


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
    return render_template('clips.html')


app.run(host="0.0.0.0", port=80, debug=True)
