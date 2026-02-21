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

class EventCreatePrev(EventBase):
    eventDate: datetime
    ubication: str
    price: int

class EventDefinitive(EventCreate):
    id: int

class EventBuy(EventDefinitive):
    user_id: int