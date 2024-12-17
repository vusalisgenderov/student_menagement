from pydantic import BaseModel

class Usercreateshcema(BaseModel):
    username:str
    password:str
    role:str
    class Config:
        extra="forbid"

class Userdeletescheme(BaseModel):
    username:str
    class Config:
        extra="forbid"


