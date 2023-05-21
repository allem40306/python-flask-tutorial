from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    name = db.Column(db.VARCHAR(30), primary_key = True)
    email = db.Column(db.VARCHAR(30))
    office = db.Column(db.VARCHAR(30))

class ClassRoom(db.Model):
    __tablename__ ='classroom'
    id = db.Column(db.INT, primary_key = True)
    floor = db.Column(db.INT)
    capacity = db.Column(db.INT)

class Course(db.Model):
    __tablename__ = 'course'
    name = db.Column(db.VARCHAR(30), primary_key = True)
    teacher = db.Column(db.VARCHAR(30), db.ForeignKey("teacher.name"))
    classRoom = db.Column(db.INT, db.ForeignKey("classroom.id"))

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