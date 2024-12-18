from fastapi import Depends
from models import *
from sqlalchemy.orm import Session
from exceptions import *
from user_schema import *
from jwt import get_current_user
import bcrypt



def get_this_user(current_user = Depends(get_current_user)):
    return current_user

def create_user_in_base(data:Usercreateshcema,db:Session):
    hashed_password=bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt())
    new_user = User(username=data.username,password=hashed_password.decode("utf-8"),role=data.role,is_deleted = False)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg":"user is created"}

def delete_user_in_base(data:Userdeletescheme,db:Session,current_user = Depends(get_current_user)):
    this_user = db.query(User).filter_by(username = current_user['username']).first()
    user = db.query(User).filter_by(username = data.username).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    if not user:
        raise UserNottFoundException
    
    if user.role == "admin":
        raise Unauthorized
    
    db.query(User).filter_by(username=data.username).update({"is_deleted": True})
    db.commit()

    return {"msg":"user is deleted"}
