from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services import faculty_service
from backend.schemas import FacultyCreate, FacultyResponse

from backend.dependencies import require_role
from backend.dependencies.db import get_db
from backend.models import AdminRole

from backend.core import limiter

router = APIRouter(prefix="/faculties", tags=["Faculties"])

# only what’s in FacultyResponse is returned.
@router.post(
    "/", 
    response_model=FacultyResponse,
    summary="Create faculty",
    description="Create a new faculty member with the provided details."
)
@limiter.limit("3/second")
async def create_faculty(
        request: Request,
        faculty: FacultyCreate,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):
    
    # create_course not belongs to this function it's belongs to sevice folder
    return await faculty_service.create_faculty(db, faculty)
    

@router.get(
    "/", 
    response_model=list[FacultyResponse],
    summary="Get all faculties",
    description="Retrieve a list of all faculty members."
)
@limiter.limit("3/second")
async def get_all_faculties(
        request: Request,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await faculty_service.get_all_faculties(db)
    

@router.get(
    "/{faculty_id}", 
    response_model=FacultyResponse,
    summary="Get faculty by ID",
    description="Retrieve details of a specific faculty member using their ID."
)
@limiter.limit("3/second")
async def get_faculty_by_id(
        request: Request,
        faculty_id: int,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await faculty_service.get_faculty_by_id(db, faculty_id)
    
    
@router.delete(
    "/{faculty_id}", 
    response_model=FacultyResponse,
    summary="Delete faculty",
    description="Delete a specific faculty member using the faculty ID."
)
@limiter.limit("2/second")
async def delete_faculty(
        request: Request,
        faculty_id: int,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):
     
    return await faculty_service.delete_faculty(db, faculty_id)