from jose import JWTError,jwt 
from passlib.context import CryptContext 
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer 
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import User
import bcrypt


SECRET_KEY = "7ff9b67b4b584ab0be8422b0fc5ff279dfc2011ef424655bee89401a9b6f6a04"



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def get_user(db:Session, username: str):
    user = db.query(User).filter_by(username=username,is_deleted = False).first()
    if user:
        return user
    
def authenticate_user(db:Session, username: str, password: str):
    user = get_user(db, username)
    if not user :
        return False
    if not bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8")):        
        return False 
    return user 


def create_access_token(data, expires_delta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire}) 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256") 
    return encoded_jwt
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401,detail="Could not validate credentials")
    return {"username":username}