from sqlalchemy.orm import Session
from app.models.ticketModel import Ticket
from fastapi import HTTPException

def fetchMyTickets(db:Session, event_id: int, user_id: int):
    tickets = (db.query(Ticket).filter(Ticket.event_id == event_id, Ticket.user_id == user_id).all())

    if not tickets:
        raise HTTPException(status_code=404, detail='No ticket found')
    
    return tickets