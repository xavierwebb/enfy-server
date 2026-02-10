from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import userService
from app.schemas.userSchema import UserDefinitive, UserReg
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

@router.post('/createUser')
def create_user(data: UserReg, db: Session = Depends(get_db)):
    db_user = userService.get_userByEmail(db, data.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    return userService.create_user(db, data)