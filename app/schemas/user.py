from pydantic import BaseModel,Field,EmailStr
from enum import Enum




class UserRole(str,Enum):
    admin="admin"
    student="student"
    teacher="teacher"

class UserSchema(BaseModel):
    name:str= Field(min_length=3,max_length=50)
    email:EmailStr=Field(examples=["user@gmail.com"])
    password:str = Field(min_length=8,examples=["12345678"])
    role:UserRole

class LoginSchema(BaseModel):
    email:EmailStr
    password:str