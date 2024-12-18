from sqlalchemy import Column,Integer,String,Date,Boolean
from db import Base,engine


class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)
    role = Column(String)
    is_deleted = Column(Boolean)


class Student(Base):
    __tablename__="students"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    surname = Column(String)
    fin_code = Column(String,unique=True)
    Birth_date = Column (Date)
    is_deleted = Column(Boolean)
    
class Course(Base):
    __tablename__="courses"
    id = Column(Integer,primary_key=True)
    teacher_id = Column(Integer)
    subject = Column(String)
    description_of_subject = Column(String)
    is_deleted = Column(Boolean)

class Registration(Base):
    __tablename__="student_course_registration"
    id = Column(Integer,primary_key=True)
    course_name = Column(String)
    student_id = Column(Integer)
    final_marks = Column(Integer)
    is_deleted = Column(Boolean)

Base.metadata.create_all(bind=engine)