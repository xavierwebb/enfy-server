from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.eventSchema import EventCreate, EventBuy
from app.services.eventSevice import createEvent, buyEvent

router = APIRouter(
    prefix='/events',
    tags=['events']
)

@router.post('/createEvent')
def create_event(data: EventCreate, db: Session = Depends(get_db)):
    event = createEvent(db, data)
    return event

@router.post('/buyEvent')
def buy_event(data: EventBuy,db: Session = Depends(get_db)):
    event = buyEvent(db, data)
    return event