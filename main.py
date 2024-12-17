from fastapi import FastAPI,Depends
from login import login_router
from user import user_router
from user_service import *
from db import get_db
app = FastAPI()


@app.get("/")
def health_check():
    return {'msg':"heath_check is succsesfull"}




app.include_router(login_router)
app.include_router(user_router)