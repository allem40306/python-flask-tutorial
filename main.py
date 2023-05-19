from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/json/')
def json():
    data = {"messenger":"Hello, World!"}
    return jsonify(data)


@app.route('/json/<int:test_id>/')
def json_with_id(test_id):
    data = {"id": test_id}
    return jsonify(data)