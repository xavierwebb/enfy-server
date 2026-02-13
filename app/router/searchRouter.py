from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.searchService import search_content

router = APIRouter(
    prefix='/search',
    tags=['search']
)

@router.get('/searchEvent/{contentSearched}')
def search_event(contentSearched: str ,db: Session = Depends(get_db)):
    content = search_content(db, contentSearched)
    return content