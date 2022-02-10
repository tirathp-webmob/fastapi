import email
from unicodedata import name
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from typing import Optional

from sqlalchemy import Column, Integer
# Post is a class, which basically inherits from BaseModel class.




class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserCreateResponse(BaseModel):
    email: EmailStr
    id: int

    class Config:
        orm_mode = True


class Userget(UserCreateResponse):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Post(BaseModel):
    name: str
    company: str
    
    email: Optional[str] = None


class PostCreate(Post):
    pass

class PostResponse(PostCreate):
    id: int
    owner_id: int
    owner: UserCreateResponse
    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post :PostResponse 
    votes : int

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)