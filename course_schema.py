from pydantic import BaseModel


class LessonCreateSchema(BaseModel):
    subject:str
    description_of_subject:str
    teacher_id:int
    class Config:
        extra = "forbid"


class LessonRegistrSchema(BaseModel):
    course_name:str
    student_id:int
    class Config:
        extra = "forbid"

class LessonDeleteSchema(BaseModel):
    course_id:int
    
    class Config:
        extra = "forbid"
