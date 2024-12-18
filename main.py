from fastapi import FastAPI,Depends
from login import login_router
from user import user_router
from student import student_router
from course import course_router
app = FastAPI()


@app.get("/")
def heaalth_check():
    return {'msg':"heath_check is succsesfull"}



app.include_router(course_router)
app.include_router(student_router)
app.include_router(user_router)
app.include_router(login_router)