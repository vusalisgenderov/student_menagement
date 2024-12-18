from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from jwt import get_current_user
from course_schema import *
from course_service import *
from db import get_db

course_router = APIRouter(tags=["course"],prefix="/course")


@course_router.get("/")
def get_all_course(db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = get_all_course_in_base(db=db,current_user=current_user)
    return msg


@course_router.post("/")
def create_course(item:LessonCreateSchema,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = create_course_in_base(db=db,data=item,current_user=current_user)
    return msg


@course_router.post("/register_course")
def registr_course(item:LessonRegistrSchema,db:Session=Depends(get_db),current_user = Depends(get_current_user)):
    msg = create_registr_course(db=db,data=item,current_user=current_user)
    return msg


@course_router.delete("/{id}")
def delete_course(item:LessonDeleteSchema,db:Session=Depends(get_db),current_user = Depends(get_current_user)):
    msg = delete_course_by_id(db=db,data=item,current_user=current_user)
    return msg