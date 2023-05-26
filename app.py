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
    __tablename__ = "teacher"
    name = db.Column(db.VARCHAR(30), primary_key = True, nullable = False)
    email = db.Column(db.VARCHAR(30), nullable = False)
    office = db.Column(db.VARCHAR(30), nullable = False)
    course = db.relationship("Course", backref = "teacherInfo")

    def __init__(self, name, email, office):
        self.name = name
        self.email = email
        self.office = office

class Classroom(db.Model):
    __tablename__ = "classroom"
    id = db.Column(db.VARCHAR(30), primary_key = True, nullable = False)
    floor = db.Column(db.INT, nullable = False)
    capacity = db.Column(db.INT, nullable = False)
    course = db.relationship("Course", backref = "classroomInfo")

    def __init__(self, id, floor, capacity):
        self.id = id
        self.floor = floor
        self.capacity = capacity

class Course(db.Model):
    __tablename__ = "course"
    name = db.Column(db.VARCHAR(30), primary_key = True)
    teacher = db.Column(db.VARCHAR(30), db.ForeignKey("teacher.name"), nullable = False)
    roomCode = db.Column(db.VARCHAR(30), db.ForeignKey("classroom.id"), nullable = False)

    def __init__(self, name, teacher, roomCode):
        self.name = name
        self.teacher = teacher
        self.roomCode = roomCode

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
    return data

@app.route('/create')
def create():
    classroom1 = Classroom("CD321", 5, 20)
    classroom2 = Classroom("CD322", 4, 22)
    teacher1 = Teacher(name = "Sam", email = "sam@test.com", office = "AB123")
    teacher2 = Teacher(name = "Ann", email = "ann@test.com", office = "AB124")
    course1 = Course("Data Structure", "Sam", "CD321")
    course2 = Course("Algorithm", "Ann", "CD322")

    db.session.add(classroom1)

    data = [classroom2, teacher1, teacher2]
    db.session.add_all(data)

    db.session.add_all([course1, course2])
    db.session.commit()
    
    return "OK Success"

@app.route('/select')
def select():
    print(Course.__tablename__)
    res1 = Course.query.filter_by(name = "Algorithm").first()
    print(f"Course: {res1.name, res1.teacher, res1.roomCode}")
    print(f"teacher: {res1.teacherInfo.email, res1.teacherInfo.office}")
    
    res2 = Teacher.query.all()
    for res in res2:
        print(res.name, res.email, res.office)

    return "OK Success"

@app.route('/update')
def update():
    query = Course.query.filter_by(name = "Algorithm").first()
    query.roomCode = "CD321"
    db.session.commit()

    return "OK Success"

@app.route('/delete')
def delete():
    query = Course.query.filter_by(name = "Algorithm").first()
    db.session.delete(query)
    db.session.commit()

    return "OK Success"
