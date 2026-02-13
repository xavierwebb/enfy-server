from sqlalchemy.orm import Session
from app.models.eventModel import Event
from sqlalchemy import or_
from fastapi import HTTPException

def search_content(db: Session, content: str):
    contentSearched = db.query(Event).filter(
        or_(
            Event.name.ilike(f'%{content}%'),
            Event.description.ilike(f'%{content}%')
        )
    ).all()

    if not contentSearched:
        raise HTTPException(status_code=404, detail='Event not found')

    return contentSearched