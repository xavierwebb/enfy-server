from fastapi import APIRouter, Depends, Cookie
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.ticketsService import fetchMyTickets
from app.services.authService import check_token
router = APIRouter(prefix='/tickets', tags=['tickets'])

@router.get('/fetchMyTickets/{event_id}')
def fetch_my_tickets(event_id: int, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    user_id = check_token(access_token)
    return fetchMyTickets(db, event_id, user_id)