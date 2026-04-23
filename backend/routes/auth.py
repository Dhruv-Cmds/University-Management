from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.schemas import AdminLogin, AdminCreate, AdminResponse
from backend.services import admin_service, login_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/login")
def login(admin_data: AdminLogin, db: Session = Depends(get_db)):

    try:
        return login_admin(
            db,
            admin_data.email,
            admin_data.password
        )

    except ValueError as e:
        
        raise HTTPException(status_code=401, detail=str(e))
    


@router.post("/signup", response_model=AdminResponse)
def signup(admin_data: AdminCreate, db: Session = Depends(get_db)):
    try:
        return admin_service.create_admin(db, admin_data)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))