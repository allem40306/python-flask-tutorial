from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import configparser

config = configparser.ConfigParser()
config.read_file(open("dev.ini"))
username = config.get('DATABASE', 'username')
password = config.get('DATABASE', 'password')
host = config.get('DATABASE', 'host')
port = config.get('DATABASE', 'port')
database = config.get('DATABASE', 'database')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
db = SQLAlchemy(app)

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


@app.route('/table/')
def show_table():
    sql_cmd = text("show tables")
    result = db.session.execute(sql_cmd)
    data = [row[0] for row in result]
    print(data)
    return data