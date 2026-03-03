from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    name: str
    description: str

class EventCreate(EventBase):
    eventDate: datetime
    ubication: str
    owner_id: int
    price: int
    category: str

class EventCreatePrev(EventBase):
    eventDate: datetime
    ubication: str
    price: int
    category: str

class EventDefinitive(EventCreate):
    id: int
    status: str

class EventBuy(BaseModel):
    id: int
    master_card: int
    security_number: int