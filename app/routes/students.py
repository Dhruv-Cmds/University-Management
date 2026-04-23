from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services import student_service
from app.schemas import StudentCreate, StudentResponse

from app.dependencies import get_db, require_role
from app.models import AdminRole


router = APIRouter(prefix="/students", tags=["Students"])

# only what’s in StudentResponse is returned.
@router.post("/", response_model = StudentResponse)
def create_student(
                student: StudentCreate,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin]))
            ):

    try:
        # create_course not belongs to this function it's belongs to sevice folder
        return student_service.create_student(db, student)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model= list[StudentResponse])
def get_all_students(
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                ):

    try:

        return student_service.get_all_students(db)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{student_id}", response_model= StudentResponse)
def get_student_by_id(
                    student_id: int,
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                ):

    try:

        return student_service.get_student_by_id(db, student_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
    
@router.delete("/{student_id}", response_model= StudentResponse)
def delete_student(
                student_id: int,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin]))
            ):
     
    try:

        return student_service.delete_student(db, student_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
