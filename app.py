from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

prompttxt = None


@app.route("/")
def index():
    return render_template('index.html', prompttxt=prompttxt)


@app.route("/prompt", methods=["POST"])
def prompt():
    global prompttxt
    prompttxt = request.form['prompttxt']
    return redirect(url_for("index"))


app.run(host="0.0.0.0", port=80, debug=True)
