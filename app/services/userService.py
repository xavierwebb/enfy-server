from sqlalchemy.orm import joinedload, with_loader_criteria, Session
from app.models.userModel import User
from app.schemas.userSchema import UserReg, AplicationCreation
from app.services.authService import hash_password, create_access_token
from fastapi import HTTPException
from app.models.aplicationsModel import Aplications
from app.models.eventModel import Event

def get_userById(db: Session, id: int):
    user = db.query(User).options(
        joinedload(User.eventsCreated),
        joinedload(User.eventsBought),
        with_loader_criteria(Event, Event.status == 'active')
    ).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user

def get_userByEmail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, userData: UserReg):
    hashed_password = hash_password(userData.password)

    db_user = User(
        name=userData.name,
        email=userData.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit() 
    db.refresh(db_user)
    
    token = create_access_token({
        'sub': str(db_user.id)
    })

    return {
        'user': db_user,
        'access_token': token,
        'token_type': 'bearer'
    }

def create_aplication(db: Session, data: AplicationCreation):
    db_app = Aplications(
        user_id = data.user_id,
        name=data.name,
        contact=data.contact,
        theme=data.theme
    )

    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return {'detail':'Aplication created!'}