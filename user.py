from fastapi import APIRouter,Depends
from jwt import get_current_user
from user_service import *
from db import get_db

user_router = APIRouter(tags=["user"],prefix="/user")


@user_router.get("/")
def get_user(current_user = Depends(get_current_user)):
    msg = get_this_user(current_user=current_user)
    return msg


@user_router.post("/")
def create_user(item:Usercreateshcema,db:Session = Depends(get_db)):
    msg = create_user_in_base(data=item,db=db)
    return msg


@user_router.delete("/")
def delete_user(item:Userdeletescheme,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    msg = delete_user_in_base(data=item,db=db,current_user = current_user)
    return msg



