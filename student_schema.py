from pydantic import BaseModel
from datetime import date

class Studentcreateshcema(BaseModel):
    name:str
    surname:str
    fin_code:str
    birth_date:date
    class Config:
        extra="forbid"

class Studentdeletescheme(BaseModel):
    id:int
    class Config:
        extra="forbid"