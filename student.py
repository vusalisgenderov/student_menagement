from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from jwt import get_current_user
from student_schema import *
from student_service import *
from db import get_db

student_router = APIRouter(tags=["students"],prefix="/students")


@student_router.get("/")
def get_all_students(db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = get_all_students_in_db(db=db,current_user=current_user)
    return msg

@student_router.get("/{id}")
def get_student_by_id(id:int,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = get_student_by_id_in_base(id=id,db=db,current_user=current_user)
    return msg


@student_router.post("/")
def create_student(item:Studentcreateshcema,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = create_student_in_base(db=db,data=item,current_user=current_user)
    return msg

@student_router.delete("/")
def delete_student(item:Studentdeletescheme,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = delete_student_by_id(db=db,data=item,current_user=current_user)
    return msg