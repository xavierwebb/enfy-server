from pydantic import BaseModel, EmailStr
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
    class Config:
        from_attributes = True

class UserFetch(UserBase):
    id: int
    email: str
    createdAt: datetime
    eventsCreated: List[EventDefinitive]

class UserLog(BaseModel):
    email: str
    password: str

class UserReg(UserBase):
    email: EmailStr
    password: str
