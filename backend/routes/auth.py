from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.schemas import AdminLogin, AdminCreate, AdminResponse
from backend.models import AdminRole

from backend.services import admin_service, login_admin
from backend.dependencies import get_db, require_role

from backend.core import limiter


router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/signup", response_model=AdminResponse)
@limiter.limit("3/second")
async def create_admin(
    request: Request, 
    admin_data: AdminCreate,
    db: AsyncSession = Depends(get_db)):

    return await admin_service.create_admin(db, admin_data)


@router.post("/login")
@limiter.limit("5/minute")
async def login(
    request: Request, 
    admin_data: AdminLogin,
    db: AsyncSession = Depends(get_db)):

    return login_admin(
        db,
        admin_data.email,
        admin_data.password
    )


@router.get("/", response_model= list[AdminResponse])
@limiter.limit("3/second")
async def get_all_admin(
        request: Request,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):


    return await admin_service.get_all_admin(db)

    
@router.get("/{admin_id}", response_model= AdminResponse)
@limiter.limit("3/second")
async def get_admin_by_id(
        request: Request, 
        admin_id: int,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):

    return await admin_service.get_admin_by_id(db, admin_id)
    
@router.delete("/{admin_id}", response_model= AdminResponse)
@limiter.limit("2/second")
async def delete_admin_by_id(
        request: Request, 
        course_id: int,
        db:AsyncSession = Depends(get_db),
        current_user = Depends(require_role([AdminRole.admin]))
    ):

    return await admin_service.delete_admin_by_id(db, course_id)
