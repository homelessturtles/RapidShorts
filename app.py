from flask import Flask, render_template, request, url_for, redirect
from script_gen import generate_script_sample

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/script", methods=["POST"])
def script():
    prompttxt = request.form['prompttxt']
    generated_script = generate_script_sample(prompttxt)
    return render_template('script.html', scripttxt=generated_script)


app.run(host="0.0.0.0", port=80, debug=True)
