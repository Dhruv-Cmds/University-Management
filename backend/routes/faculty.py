from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.services import faculty_service
from backend.schemas import FacultyCreate, FacultyResponse

from backend.dependencies import get_db, require_role
from backend.models import AdminRole

router = APIRouter(prefix="/faculties", tags=["Faculties"])

# only what’s in FacultyResponse is returned.
@router.post("/", response_model = FacultyResponse)
def create_faculty(
                faculty: FacultyCreate,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin]))
            ):

    try:
        # create_course not belongs to this function it's belongs to sevice folder
        return faculty_service.create_faculty(db, faculty)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model= list[FacultyResponse])
def get_all_faculties(
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                ):

    try:

        return faculty_service.get_all_faculties(db)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{faculty_id}", response_model= FacultyResponse)
def get_faculty_by_id(
                    faculty_id: int,
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                ):

    try:

        return faculty_service.get_faculty_by_id(db, faculty_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
    
@router.delete("/{faculty_id}", response_model= FacultyResponse)
def delete_faculty(
                faculty_id: int,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin]))
            ):
     
    try:

        return faculty_service.delete_faculty(db, faculty_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
