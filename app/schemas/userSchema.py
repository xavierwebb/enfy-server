from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: str

class UserDefinitive(UserBase):
    id: int
    email: str
    createdAt: datetime

    class Config:
        from_attributes = True


class UserLog(UserBase):
    password: str

class UserReg(UserBase):
    email: EmailStr
    password: str
