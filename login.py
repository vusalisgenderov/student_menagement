from fastapi import APIRouter,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm #front send the password correct way using our api
from jwt import authenticate_user,create_access_token,get_current_user
from db import get_db
from datetime import timedelta
from sqlalchemy.orm import Session


login_router = APIRouter(tags=["Authorization"])


@login_router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@login_router.get("/me")
def read_users_me(current_user = Depends(get_current_user)):
    return current_user
