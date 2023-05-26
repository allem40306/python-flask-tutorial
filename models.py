from app import db

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
