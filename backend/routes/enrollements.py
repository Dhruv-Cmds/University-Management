from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services import enrollment_service
from backend.schemas import EnrollmentCreate, EnrollmentResponse

from backend.dependencies import get_db, require_role
from backend.models import AdminRole

from backend.core import limiter

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

# only what’s in EnrollmentResponse is returned.
@router.post("/", response_model = EnrollmentResponse)
@limiter.limit("3/second")
async def create_enrollment(
        request: Request,
        enrollment: EnrollmentCreate,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    # create_course not belongs to this function it's belongs to sevice folder
    return await enrollment_service.create_enrollment(db, enrollment)
    
@router.get("/", response_model= list[EnrollmentResponse])
@limiter.limit("3/second")
async def get_all_enrollments(
        request: Request,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):


    return await enrollment_service.get_all_enrollments(db)
    
@router.get("/{enrollment_id}", response_model= EnrollmentResponse)
@limiter.limit("3/second")
async def get_enrollment_by_id(
        request: Request,
        enrollment_id: int,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await enrollment_service.get_enrollment_by_id(db, enrollment_id)
    
    
@router.delete("/{enrollment_id}", response_model= EnrollmentResponse)
@limiter.limit("2/second")
async def delete_enrollment(
        request: Request,
        enrollment_id: int,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin, AdminRole.faculty]))
    ):

    return await enrollment_service.delete_enrollment(db, enrollment_id)