from sqlalchemy.orm import Session
from app.schemas.eventSchema import EventCreate, EventDefinitive, EventBuy
from app.models.eventModel import Event
from app.services.userService import get_userById
from fastapi import HTTPException

def createEvent(db: Session, data: EventCreate):
    user = get_userById(db, data.owner_id)

    event = Event(
        name=data.name,
        description=data.description,
        ubication=data.ubication,
        eventDate=data.eventDate,
        owner=user,
        price=data.price
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def searchEvent(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail='Event not found')
    
    return event

def buyEvent(db: Session, data: EventBuy):
    event = searchEvent(db, data.id)
    user = get_userById(db, data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    event.paidUsers.append(user)
    db.commit()
    db.refresh(event)

    return event