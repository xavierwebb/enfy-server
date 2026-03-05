import bcrypt
from datetime import datetime, timedelta
import jwt
from app.auth import ACCESS_TOKEN_EXPIRE_DAYS, SECRET_KEY, ALGORITHM
from fastapi import Cookie, HTTPException
from sqlalchemy.orm import Session

def hash_password(password: str):

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

def create_access_token(data: dict):
    payload = data.copy()
    payload['exp'] = datetime.now() + timedelta(
        days=ACCESS_TOKEN_EXPIRE_DAYS
    )

    token = jwt.encode(payload,SECRET_KEY, algorithm=ALGORITHM )
    return token

def check_token(token: str):
    if not token:
        raise HTTPException(status_code=404, detail='There is no Token')
    
    tokenPayload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )
    
    return tokenPayload.get('sub')

def check_admin(db: Session, access_token: str):
    from app.services.userService import get_userById
    user_id = check_token(access_token)
    user = get_userById(db, user_id)

    if not user.role == 'Admin':
        raise HTTPException(status_code=403, detail='You are not authorized for make this action')
    
    return
