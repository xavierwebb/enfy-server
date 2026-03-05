from pydantic import BaseModel, EmailStr
from fastapi import File
from datetime import datetime
from app.schemas.eventSchema import EventDefinitive
from typing import List

class UserBase(BaseModel):
    name: str

class UserDefinitive(UserBase):
    id: int
    email: str
    role: str
    createdAt: datetime
    eventsBought: List[EventDefinitive]
    eventsCreated: List[EventDefinitive]
    profilePicture: str
    class Config:
        from_attributes = True

class UserFetch(UserBase):
    id: int
    role: str
    profilePicture: str
    createdAt: datetime
    eventsCreated: List[EventDefinitive]

class UserLog(BaseModel):
    email: str
    password: str

class UserReg(UserBase):
    email: EmailStr
    password: str
    categories: List[str]

class Aplication(BaseModel):
    name: str
    contact: str
    theme: str

class AplicationCreation(Aplication):
    user_id: int

class AplicationAcceptReject(BaseModel):
    id: int