from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services import student_service
from backend.schemas import StudentCreate, StudentResponse

from backend.dependencies import get_db, require_role
from backend.models import AdminRole

from backend.core import limiter

router = APIRouter(prefix="/students", tags=["Students"])

# only what’s in StudentResponse is returned.
@router.post(
    "/", 
    response_model=StudentResponse,
    summary="Create student",
    description="Create a new student with the provided details."
)
@limiter.limit("3/second")
async def create_student(
        request: Request,
        student: StudentCreate,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):

    # create_course not belongs to this function it's belongs to sevice folder
    return await student_service.create_student(db, student)
    

@router.get(
    "/", 
    response_model=list[StudentResponse],
    summary="Get all students",
    description="Retrieve a list of all students."
)
@limiter.limit("3/second")
async def get_all_students(
        request: Request,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await student_service.get_all_students(db)
    

@router.get(
    "/{student_id}", 
    response_model=StudentResponse,
    summary="Get student by ID",
    description="Retrieve details of a specific student using their ID."
)
@limiter.limit("3/second")
async def get_student_by_id(
        request: Request,
        student_id: int,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await student_service.get_student_by_id(db, student_id)
    

@router.delete(
    "/{student_id}", 
    response_model=StudentResponse,
    summary="Delete student",
    description="Delete a specific student using the student ID."
)
@limiter.limit("2/second")
async def delete_student(
        request: Request,
        student_id: int,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):
     
    return await student_service.delete_student(db, student_id)