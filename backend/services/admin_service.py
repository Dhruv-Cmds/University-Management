from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from backend.models import Admin
from backend.schemas import AdminCreate

from backend.core import hash_password


async def create_admin(db: AsyncSession, admin_data: AdminCreate):

    result = await db.execute(
        select(Admin)
        .where(Admin.email == admin_data.email)
    )

    
    # scalar_one_or_none = Give me one object if found, otherwise give None
    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_admin = Admin(
        email=admin_data.email,
        password=hash_password(admin_data.password),
        role=admin_data.role
    )

    try:

        db.add(new_admin)
        await db.commit()
        await db.refresh(new_admin)

    except IntegrityError:

        await db.rollback()
        
        raise HTTPException(
            status_code=400,
            detail="Database integrity error"
        )
        
    return new_admin


async def get_all_admin(db: AsyncSession):

    result  = await db.execute(
        select(Admin)
    )

    admins = result.scalars().all()
    
    return admins

async def get_admin_by_id (db: AsyncSession, admin_id: int):

    result = await db.execute(
        select(Admin)
        .where(Admin.id == admin_id)
    )

    admin = result.scalar_one_or_none()

    if not admin:

        raise HTTPException (
            status_code=404,
            detail="Admin not found"
        )
    
    return admin

async def delete_admin_by_id(db: AsyncSession, admin_id: int):

    result = await db.execute(
        select(Admin)
        .where(Admin.id == admin_id)
    )

    admin = result.scalar_one_or_none()

    if not admin:

        raise HTTPException (
            status_code=404,
            detail="Admin not found"
        )
    
    try:

        await db.delete(admin)
        await db.commit()

    except SQLAlchemyError:

        await db.rollback()

        raise HTTPException (
            status_code=500,
            detail="Database error"
        )
    
    return admin