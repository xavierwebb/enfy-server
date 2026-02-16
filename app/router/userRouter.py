from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import userService
from app.schemas.userSchema import UserDefinitive, UserReg, UserLog, UserResponse
from app.services.authService import verify_password, create_access_token
router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/getUserById/{user_id}', response_model=UserDefinitive)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = userService.get_userById(db,user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return user

@router.post('/createUser', response_model=UserResponse)
def create_user(data: UserReg, db: Session = Depends(get_db)):
    db_user = userService.get_userByEmail(db, data.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    result = userService.create_user(db, data)
    
    return {
        'user': result['user'],
        'token': result['access_token'],
        'token_type': result['token_type']
    }

@router.post('/loginUser', response_model=UserResponse)
def login_user(data: UserLog, db: Session = Depends(get_db)):
    db_user = userService.get_userByEmail(db, data.email)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    
    confirmPass = verify_password(data.password, db_user.password)
    if (confirmPass == True):
        token = create_access_token({
            'sub': db_user.id
        })
        return {
            'user': db_user,
            'token': token,
            'token_type': 'bearer'
        }
    
    raise HTTPException(status_code=401, detail='Incorrect password')
