from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services import course_service
from backend.schemas import CourseCreate, CourseResponse

from backend.dependencies import get_db, require_role
from backend.models import AdminRole

from backend.core import limiter

router = APIRouter(prefix="/courses", tags=["Courses"])

# only what’s in CourseResponse is returned.
@router.post(
    "/", 
    response_model=CourseResponse,
    summary="Create course",
    description="Create a new course with the provided course details."
)
@limiter.limit("3/second")
async def create_course(
        request: Request,
        course: CourseCreate,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(
            require_role([AdminRole.admin, AdminRole.faculty])
        )
    ):

    # create_course not belongs to this function it's belongs to sevice folder
    return await course_service.create_course(db, course)
    
    
@router.get(
    "/", 
    response_model=list[CourseResponse],
    summary="Get all courses",
    description="Retrieve a list of all available courses."
)
@limiter.limit("3/second")
async def get_all_courses(
        request: Request,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
):

    return await course_service.get_all_courses(db)
    
    
@router.get(
    "/{course_id}", 
    response_model=CourseResponse,
    summary="Get course by ID",
    description="Retrieve details of a specific course using its ID."
)
@limiter.limit("3/second")
async def get_course_by_id(
        request: Request,
        course_id: int,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await course_service.get_course_by_id(db, course_id)
    
    
@router.delete(
    "/{course_id}", 
    response_model=CourseResponse,
    summary="Delete course",
    description="Delete a specific course using the course ID."
)
@limiter.limit("2/second")
async def delete_course(
        request: Request,
        course_id: int,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):
    
    return await course_service.delete_course(db, course_id)