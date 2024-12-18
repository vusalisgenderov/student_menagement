from fastapi import Depends
from models import *
from jwt import get_current_user
from sqlalchemy.orm import Session
from exceptions import *
from course_schema import *
from datetime import date



def get_all_course_in_base(db:Session , current_user = Depends(get_current_user)):
    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    all_courses = db.query(Course).filter_by(is_deleted = False).all()
    all_courses_names = []

    for course in all_courses:
        all_courses_names.append(course.subject)

    return {"all course" : all_courses_names}




def get_course_info_for_lecture_by_id(course_id:int,db:Session , current_user = Depends(get_current_user)):
    pass





def create_course_in_base(db:Session, data:LessonCreateSchema, current_user = Depends(get_current_user)):
    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    check_user_role = db.query(User).filter_by(id = data.teacher_id).first()

    if not check_user_role:
        raise UserNottFoundException

    if check_user_role.role == "admin":
        raise HTTPException(status_code=403,detail="only it can be assigned to teachers")
    
    
    check_course_exist = db.query(Course).filter_by(subject = data.subject ,teacher_id = data.teacher_id).first()

    if check_course_exist:
        raise CourseIsExists

    new_course = Course(subject = data.subject ,teacher_id = data.teacher_id, description_of_subject = data.description_of_subject, is_deleted = False)

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return {"msg":"course is created"}
    






def create_registr_course(db:Session,data:LessonRegistrSchema,current_user = Depends(get_current_user)):
    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    check_course_exist = db.query(Course).filter_by(subject = data.course_name).first()

    if not check_course_exist:
        raise CourseNotFoundException
    
    check_student_exist = db.query(Student).filter_by(id = data.student_id,is_deleted = False).first()

    if not check_student_exist:
        raise StudentNotFoundException
    
    check_student_exist_in_course = db.query(Registration).filter_by(student_id = data.student_id).first()
    
    if check_student_exist_in_course:
        raise StudentIsExists

    new_user = Registration(course_name = data.course_name,student_id = data.student_id,is_deleted = False)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg":"student is added into course"}



def delete_course_by_id(db:Session,data:LessonDeleteSchema,current_user = Depends(get_current_user)):
    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    check_lesson_in_course = db.query(Course).filter_by(id = data.course_id).first()

    if not check_lesson_in_course:
        raise CourseNotFoundException
    
    check_lesson_in_registr = db.query(Registration).filter_by(course_name = check_lesson_in_course.subject,is_deleted = False).first()

    if check_lesson_in_registr:
        raise HTTPException(status_code=401,detail="this course can't delete")
    
    db.query(Course).filter_by(id = data.course_id).update({"is_deleted":True})
    db.commit()

    return {"msg":"lesson is deleted"}

    