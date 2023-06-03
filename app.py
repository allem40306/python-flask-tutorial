from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

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
    print(Course.__tablename__) # 可以輸出 Model 的 Metadata
    res1 = Course.query.filter_by(name = "Algorithm").first()
    print(f"Course: {res1.name, res1.teacher, res1.roomCode}")
    print(f"teacher: {res1.teacherInfo.email, res1.teacherInfo.office}")  # 輸出課程教師的相關資訊
    
    res2 = Teacher.query.all()
    for res in res2:
        print(res.name, res.email, res.office)

    return "OK Success"

@app.route('/update')
def update():
    res = Course.query.filter_by(name = "Algorithm").first()
    res.roomCode = "CD321"

    res = Course.query.all()
    for r in res:
        r.roomCode = "CD322"
    
    db.session.commit()
    
    return "OK Success"

@app.route('/delete')
def delete():
    res = Course.query.filter_by(name = "Algorithm").first()
    db.session.delete(res)
    db.session.commit()

    res = Course.query.all()
    for r in res:
        db.session.delete(r)
    db.session.commit()

    return "OK Success"
