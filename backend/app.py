from flask import Flask, request, jsonify, send_from_directory
from test import test
import os

app = Flask(__name__)

frontend_folder = os.path.join(os.getcwd(), "..", "frontend")
dist_folder = os.path.join(frontend_folder, "dist")


@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(dist_folder, filename)


@app.route("/api/process_prompt", methods=['POST'])
def process_prompt_fun():
    data = request.get_json()
    prompt = data.get('prompt')
    url = test(prompt)
    return jsonify({"video": url})


if __name__ == '__main__':
    app.run(debug=True)
