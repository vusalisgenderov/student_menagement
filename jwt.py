#json web token
from jose import JWTError,jwt #library for implementing jwt
from passlib.context import CryptContext #for hashing password
from fastapi import HTTPException, Depends #dependency injection
from fastapi.security import OAuth2PasswordBearer # mechanism for exchanging passwords between front end and backend
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import User
import bcrypt


SECRET_KEY = "7ff9b67b4b584ab0be8422b0fc5ff279dfc2011ef424655bee89401a9b6f6a04"
# for signing JWT and verifying its originality
# dont store credentials in code


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def get_user(db:Session, username: str):
    user = db.query(User).filter_by(username=username).first()
    if user:
        return user
    
def authenticate_user(db:Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False #user does not exist in our system
    if not bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8")):        
        return False #user entered wrong password
    return user #success, user is authenticated


def create_access_token(data, expires_delta = None):
    to_encode = data.copy() #{"sub": username}
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire}) #now jwt payload has username and expire date
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256") 
    return encoded_jwt #our jwt token

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401,detail="Could not validate credentials")
    return {"username":username}
