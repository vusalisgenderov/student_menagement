from models import *
from sqlalchemy.orm import Session
from exceptions import *
from setting import DATABASE_URL
from schema import *
from datetime import date
import bcrypt



def creat_user_in_base(data:Usercreateshcema,db:Session):
    hashed_password=bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt())
    new_user = User(username=data.username,password=hashed_password.decode("utf-8"),role=data.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg":"user is created"}
