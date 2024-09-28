# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(name)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data')
    with open('data.txt', 'w') as f:
        f.write(data)
    return {'message': 'Данные получены'}


@app.route('/fetch', methods=['GET'])
def fetch():
    with open('data.txt', 'r') as f:
        data = f.read()
    return jsonify({'data': data})


if name == 'main':
    app.run(port=8000)
