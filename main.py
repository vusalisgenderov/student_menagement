from fastapi import FastAPI,Depends
from login import login_router
from service import *
from db import get_db
app = FastAPI()


@app.get("/")
def heaalth_check():
    return {'msg':"heath_check is succsesfull"}

@app.post("/user")
def create_user(item:Usercreateshcema,db:Session=Depends(get_db)):
    msg = creat_user_in_base(data=item,db=db)
    return msg




app.include_router(login_router)