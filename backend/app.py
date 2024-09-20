from flask import Flask, request, jsonify
from flask_cors import CORS
from test import test

app = Flask(__name__)
CORS(app)


@app.route("/api/process_prompt", methods=['POST'])
def index():
    data = request.get_json()
    prompt = data.get('prompt')
    url = test(prompt)
    return jsonify({"video": url})


if __name__ == '__main__':
    app.run(debug=True)
