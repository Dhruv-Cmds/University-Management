from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas import AdminLogin, AdminCreate, AdminResponse

from backend.services import admin_service, login_admin

from backend.dependencies import get_db, require_role

from backend.models import AdminRole


router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/signup", response_model=AdminResponse)
def create_admin(admin_data: AdminCreate, db: Session = Depends(get_db)):
    try:
        return admin_service.create_admin(db, admin_data)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


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


@router.get("/", response_model= list[AdminResponse])
def get_all_admin(
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin]))
                ):

    try:

        return admin_service.get_all_admin(db)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{admin_id}", response_model= AdminResponse)
def get_admin_by_id(
                    admin_id: int,
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin]))
                    ):

    try:

        return admin_service.get_admin_by_id(db, admin_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
    
@router.delete("/{admin_id}", response_model= AdminResponse)
def delete_admin_by_id(
                course_id: int,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin]))
                ):
    try:

        return admin_service.delete_admin_by_id(db, course_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
