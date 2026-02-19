from fastapi import HTTPException, APIRouter, Depends, Response, Cookie
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import userService
from app.schemas.userSchema import UserDefinitive, UserReg, UserLog, UserFetch
from app.services.authService import verify_password, create_access_token, check_token
router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/createUser', response_model=UserDefinitive)
def create_user(data: UserReg, response: Response, db: Session = Depends(get_db)):

    db_user = userService.get_userByEmail(db, data.email)

    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    result = userService.create_user(db, data)
    
    response.set_cookie(
        key='access_token',
        value=result['access_token'],
        httponly=True,
        secure=False,
        samesite='lax',
        max_age=900
    )


    return result['user']

@router.post('/loginUser', response_model=UserDefinitive)
def login_user(data: UserLog, response: Response, db: Session = Depends(get_db)):

    db_user = userService.get_userByEmail(db, data.email)

    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    
    confirmPass = verify_password(data.password, db_user.password)

    if (confirmPass == True):
        token = create_access_token({
            'sub': str(db_user.id)
        })

        response.set_cookie(
            key='access_token',
            value=token,
            httponly=True,
            secure=False,
            samesite='lax',
            max_age=900
        )

        return db_user
    
    raise HTTPException(status_code=401, detail='Incorrect password')

@router.get('/fetchUser/{user_id}', response_model=UserFetch)
def fetch_user(user_id: int, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    check_token(access_token)
    return userService.get_userById(db, user_id)

@router.get('/fetchMe', response_model=UserDefinitive)
def fetch_me(access_token: str = Cookie(None), db: Session = Depends(get_db)):
    
    user_id = check_token(access_token)

    return userService.get_userById(db, user_id)
