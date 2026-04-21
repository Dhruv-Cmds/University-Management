from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import UserLogin, UserCreate, UserResponse
from app.services import login_user, user_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):

    try:
        return login_user(
            db,
            user_data.email,
            user_data.password
        )

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    


@router.post("/signup", response_model=UserResponse)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user_data)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))