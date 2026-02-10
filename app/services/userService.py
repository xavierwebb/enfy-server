from sqlalchemy.orm import Session
from app.models.userModel import User
from app.schemas.userSchema import UserReg

def get_userById(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_userByEmail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, userData: UserReg):
    hashed_password = userData.password

    db_user = User(
        name=userData.name,
        email=userData.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user