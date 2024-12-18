from fastapi import Depends
from models import *
from jwt import get_current_user
from sqlalchemy.orm import Session
from exceptions import *
from student_schema import *
from datetime import date

def get_all_students_in_db(db:Session,current_user = Depends(get_current_user)):

    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized

    all_user = db.query(Student).filter_by(is_deleted = False).all()
    all_user_names = []
    for user in all_user:
        all_user_names.append(user.name)

    return {"all_user":all_user_names}

def get_student_by_id_in_base(id:int,db:Session,current_user = Depends(get_current_user)):
    
    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    student = db.query(Student).filter_by(id = id,is_deleted = False).first()

    if not student:
        raise UserNottFoundException

    student_courses = db.query(Registration).filter_by(student_id = id).all()

    courses_of_student = []

    for subject in student_courses:
        courses_of_student.append(subject.course_name)

    stud_inf = {"student_name":student.name,"student_surname":student.surname,"birth_date":student.Birth_date,"fin_code":student.fin_code,"students_courses":courses_of_student}

    return stud_inf








def create_student_in_base(db:Session,data:Studentcreateshcema,current_user = Depends(get_current_user)):
    this_student = db.query(User).filter_by(username = current_user['username']).first()

    if this_student.role != "admin":
        raise Unauthorized
    
    new_student = Student(name = data.name,surname = data.surname,fin_code = data.fin_code,Birth_date = data.birth_date,is_deleted = False)
    student = db.query(Student).filter_by(fin_code = data.fin_code).first()
    
    if student:
        raise UserIsExists
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"msg":"student is created"}

def delete_student_by_id(db:Session,data:Studentdeletescheme,current_user = Depends(get_current_user)):
    
    this_student = db.query(User).filter_by(username = current_user['username']).first()

    if this_student.role != "admin":
        raise Unauthorized
    
    student = db.query(Student).filter_by(id = data.id,is_deleted = False).first()

    if student:
        db.query(Student).filter_by(id = data.id).update({"is_deleted" : True})
        db.commit()
    else:
        raise UserNottFoundException
    
    return {"msg":"user is deleted"}
    
