# backend/app.py
from flask import Flask, request
from flask_cors import CORS

app = Flask(name)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data')
    with open('data.txt', 'w') as f:
        f.write(data)
    return {'message': 'Data received'}


if name == 'main':
    app.run(port=7000)
