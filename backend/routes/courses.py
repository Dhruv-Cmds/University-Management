from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.services import course_service
from backend.schemas import CourseCreate, CourseResponse

from backend.dependencies import get_db, require_role
from backend.models import AdminRole

router = APIRouter(prefix="/courses", tags=["Courses"])

# only what’s in CourseResponse is returned.
@router.post("/", response_model = CourseResponse)
def create_course(
                course: CourseCreate,
                db:Session = Depends(get_db),
                current_user = Depends(
                    require_role([AdminRole.admin, AdminRole.faculty])
                )
            ):

    try:
        # create_course not belongs to this function it's belongs to sevice folder
        return course_service.create_course(db, course)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model= list[CourseResponse])
def get_all_courses(
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                ):

    try:

        return course_service.get_all_courses(db)
    
    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{course_id}", response_model= CourseResponse)
def get_course_by_id(
                    course_id: int,
                    db:Session = Depends(get_db),
                    current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
                    ):

    try:

        return course_service.get_course_by_id(db, course_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
    
@router.delete("/{course_id}", response_model= CourseResponse)
def delete_course(
                course_id: int,
                db:Session = Depends(get_db),
                current_user = Depends(require_role([AdminRole.admin]))
                ):
     
    try:

        return course_service.delete_course(db, course_id)
    
    except ValueError as e:

        raise HTTPException (status_code=404, detail= str(e))
