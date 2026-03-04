from sqlalchemy.orm import Session
from app.schemas.eventSchema import EventCreate, EventBuy
from app.models.eventModel import Event
from app.services.userService import get_userById
from fastapi import HTTPException
from app.models.ticketModel import Ticket

def createEvent(db: Session, data: EventCreate):
    
    user = get_userById(db, data.owner_id)
    event = Event(
        name=data.name,
        description=data.description,
        ubication=data.ubication,
        eventDate=data.eventDate,
        owner=user,
        price=data.price,
        category= data.category
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def searchEvent(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()

    if event.status == 'finished' or event.status == 'cancelled':
        raise HTTPException(status_code=403, detail='This event is already finished')


    if not event:
        raise HTTPException(status_code=404, detail='Event not found')
    
    return event

def check_bought(db: Session, event_id: int, user_id: int) -> bool:
    return db.query(Ticket).filter(
        Ticket.event_id == event_id,
        Ticket.user_id == user_id
    ).first() is not None

def buyEvent(db: Session, data: EventBuy, user_id: int):
    event = searchEvent(db, data.id)
    user = get_userById(db, user_id)

    if event.status == 'in_progress' or event.status == 'finished' or event.status == 'cancelled':
        raise HTTPException(status_code=403, detail='You are not authorized to purchase this event due to its status')

    check = check_bought(db, data.id, user_id)

    ticket = Ticket(
        event_id = data.id,
        user_id = user_id
    )

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    if check == True:
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return

    event.paidUsers.append(user)
    db.add(ticket)
    db.commit()
    db.refresh(event)
    return event