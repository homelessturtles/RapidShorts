from flask import Flask, request, jsonify
from flask_cors import CORS
from test import test
import os

app = Flask(__name__)
CORS(app)

frontend_folder = os.path.join(os.getcwd(),"..","frontend")
dist_folder = os.path.join(frontend_folder, "dist")

@app.route("/", defaults={"filename":""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename="index.html"
    return send_from_directory(dist_folder,filename)

@app.route("/api/process_prompt", methods=['POST'])
def index():
    data = request.get_json()
    prompt = data.get('prompt')
    url = test(prompt)
    return jsonify({"video": url})


if __name__ == '__main__':
    app.run(debug=True)
