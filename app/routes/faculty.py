from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services import faculty_service
from app.schemas import FacultyCreate, FacultyResponse

from app.dependencies import get_db, require_role, get_current_user
from app.models import UserRole

router = APIRouter(prefix="/faculties", tags=["Faculties"])

# only what’s in FacultyResponse is returned.
@router.post("/", response_model = FacultyResponse)
def create_faculty(
                faculty: FacultyCreate,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([UserRole.admin]))
            ):

    try:
        # create_course not belongs to this function it's belongs to sevice folder
        return faculty_service.create_faculty(db, faculty)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model= list[FacultyResponse])
def get_all_faculties(
                    db:Session = Depends(get_db),
                    current_user = Depends(get_current_user)
                ):

    try:

        return faculty_service.get_all_faculties(db)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{faculty_id}", response_model= FacultyResponse)
def get_faculty_by_id(
                    faculty_id: int,
                    db:Session = Depends(get_db),
                    current_user = Depends(get_current_user)
                ):

    try:

        return faculty_service.get_faculty_by_id(db, faculty_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
    
@router.delete("/{faculty_id}", response_model= FacultyResponse)
def delete_faculty(
                faculty_id: int,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([UserRole.admin]))
            ):
     
    try:

        return faculty_service.delete_faculty(db, faculty_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
