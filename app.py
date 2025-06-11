from flask import Flask, jsonify
import json
#Pytest show how tests are being passed
app = Flask(__name__)

@app.route('/')
def home():
    with open('resume.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/status')
def status():
    return {"status": "ok", "version": "1.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
