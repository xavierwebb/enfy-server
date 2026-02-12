from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
router = APIRouter(
    prefix='/search',
    tags=['search']
)

@router.get('/searchEvent')
def search_event(contentSearched: str ,db: Session = Depends(get_db)):
    return