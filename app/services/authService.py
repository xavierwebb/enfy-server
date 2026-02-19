import bcrypt
from datetime import datetime, timedelta
import jwt
from app.auth import ACCESS_TOKEN_EXPIRE_DAYS, SECRET_KEY, ALGORITHM
from fastapi import Cookie, HTTPException

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