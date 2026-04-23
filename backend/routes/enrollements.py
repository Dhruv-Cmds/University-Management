from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services import enrollment_service
from app.schemas import EnrollmentCreate, EnrollmentResponse

from app.dependencies import get_db, require_role
from app.models import AdminRole

router = APIRouter(prefix="/enrollment", tags=["Enrollments"])

# only what’s in EnrollmentResponse is returned.
@router.post("/", response_model = EnrollmentResponse)
def create_enrollment(
                course: EnrollmentCreate,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
            ):

    try:
        # create_course not belongs to this function it's belongs to sevice folder
        return enrollment_service.create_enrollment(db, course)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model= list[EnrollmentResponse])
def get_all_enrollments(
                        db:Session = Depends(get_db),
                        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                    ):

    try:

        return enrollment_service.get_all_enrollments(db)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{enrollment_id}", response_model= EnrollmentResponse)
def get_enrollment_by_id(
                    enrollment_id: int,
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                ):

    try:

        return enrollment_service.get_enrollment_by_id(db, enrollment_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
    
@router.delete("/{enrollment_id}", response_model= EnrollmentResponse)
def delete_enrollment(
                enrollment_id: int,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
            ):
     
    try:

        return enrollment_service.delete_enrollment(db, enrollment_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
