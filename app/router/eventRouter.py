from fastapi import APIRouter, Depends, Cookie, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.eventSchema import EventCreate, EventBuy
from app.services.authService import check_token
from app.services.eventSevice import createEvent, buyEvent, searchEvent
from app.models.userModel import User
router = APIRouter(
    prefix='/events',
    tags=['events']
)

@router.post('/createEvent')
def create_event(data: EventCreate, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    userId = check_token(access_token)

    user = db.query(User).filter(User.id == userId).first()

    if user.role == 'Admin' or user.role == 'Company':
        event = createEvent(db, data)
        return event
    else:
        raise HTTPException(status_code=403, detail='You are not authorized to create events')

@router.post('/buyEvent')
def buy_event(data: EventBuy,db: Session = Depends(get_db)):
    event = buyEvent(db, data)
    return event

@router.get('/fetchEvent/{id}')
def fetch_event(id: int, db: Session = Depends(get_db)):
    event = searchEvent(db, id)
    return event