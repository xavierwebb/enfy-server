from fastapi import APIRouter, Cookie
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.models.aplicationsModel import Aplications
from app.services.authService import check_token, check_admin
from app.models.userModel import User
from app.schemas.userSchema import AplicationAcceptReject

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

@router.get('/view_business_aplications')
def view_business_aplications(access_token: str = Cookie(None),db: Session = Depends(get_db)):

    check_admin(db, access_token)

    return db.query(Aplications).filter(Aplications.status == 'active').all()

@router.post('/accept_application')
def application(data: AplicationAcceptReject, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    check_admin(db, access_token)

    application = db.query(Aplications).filter(Aplications.id == data.id).first()
    
    if not application:
        raise HTTPException(status_code=404, detail='Aplication not found')

    application.status = 'finished'

    user = db.query(User).filter(User.id == application.user_id).first()
    user.role = 'Company'

    db.commit()

    return {'detail':'Application Accepted!'}

@router.post('/reject_application')
def application(id: int, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    check_admin(db, access_token)

    application = db.query(Aplications).filter(Aplications.id == id).first()
    
    if not application:
        raise HTTPException(status_code=404, detail='Aplication not found')

    application.status = 'finished'

    db.commit()

    return {'detail':'Application Rejected!'}