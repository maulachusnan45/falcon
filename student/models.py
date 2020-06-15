from pony.orm import *
from datetime import date, datetime
from connection.conn import db

class Department(db.Entity):
    number = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    groups = Set("Group")
    courses = Set("Course")

    def toJSON(self):
        return {
            'number': self.number,
            'name': self.name

        }

# @pw.register_model('number', 'major')
class Group(db.Entity):
    number = PrimaryKey(int)
    major = Required(str)
    dept = Required("Department")
    students = Set("Student")
    def toJSON(self):
        return {
            'number':self.number,
            'major': self.major,
            'dept': self.dept.toJSON()

        }


# @pw.register_model('name', 'semester',  'lect_hours', 'lab_hours', 'credits')
class Course(db.Entity):
    name = Required(str)
    semester = Required(int)
    lect_hours = Required(int)
    lab_hours = Required(int)
    credits = Required(int)
    dept = Required(Department)
    students = Set("Student")
    PrimaryKey(name, semester)


# @pw.register_model('name', 'tel', 'gpa')
class Student(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    dob = Required(date)
    tel = Optional(str)
    picture = Optional(buffer, lazy=True)
    gpa = Required(float, default=0)
    group = Required(Group)
    courses = Set(Course)

    def toJSON(self):
        return {
            'id':self.id,
            'name': self.name,
            'dob': self.dob.isoformat(),
            'tel': self.tel,
            'picture': self.picture,
            'gpa': self.gpa,
            'group': self.group.toJSON()
        }
db.generate_mapping(create_tables=True)