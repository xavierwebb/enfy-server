from fastapi import APIRouter, Depends, Cookie, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.eventSchema import EventCreate, EventBuy, EventCreatePrev, EventDefinitive
from app.services.authService import check_token
from app.services.eventSevice import createEvent, buyEvent, searchEvent
from app.services.categoryService import get_categories
from app.models.userModel import User
from app.models.eventModel import Event
from sqlalchemy import or_

router = APIRouter(
    prefix='/events',
    tags=['events']
)

@router.post('/createEvent', response_model=EventDefinitive)
def create_event(data: EventCreatePrev, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    userId = check_token(access_token)
    user = db.query(User).filter(User.id == userId).first()

    newData = EventCreate(
        name = data.name,
        description = data.description,
        eventDate = data.eventDate,
        ubication = data.ubication,
        owner_id = user.id,
        price = data.price,
        category= data.category
    )
    
    if user.role == 'Admin' or user.role == 'Company':
        event = createEvent(db, newData)

        return event
    else:
        raise HTTPException(status_code=403, detail='You are not authorized to create events')

@router.post('/buyEvent')
def buy_event(data: EventBuy, access_token: str = Cookie(None),db: Session = Depends(get_db)):
    user_id = check_token(access_token)
    event = buyEvent(db, data, user_id)

    return event

@router.get('/fetchEvent/{id}', response_model=EventDefinitive)
def fetch_event(id: int, db: Session = Depends(get_db)):
    event = searchEvent(db, id)

    return event

@router.get('/fetchRecommendedEvents')
def fetch_recommended_events(access_token: str = Cookie(None), db: Session = Depends(get_db)):
    user_id = check_token(access_token)

    categories = get_categories(user_id, db)

    if not categories:
        return []

    filters = [
        Event.category.ilike(f"%{category.category}%")
        for category in categories
    ]

    events = (
        db.query(Event)
        .filter(or_(*filters))
        .all()
    )

    return events