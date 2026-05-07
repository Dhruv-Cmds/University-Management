from sqlalchemy import select, update
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

    existing = result.scalar_one_or_none()

    if existing:
        raise ValueError("Email already registered")

    new_admin = Admin(
        email=admin_data.email,
        password=hash_password(admin_data.password),
        role=admin_data.role
    )

    try:

        db.add(new_admin)
        await db.commit()
        await db.refresh(new_admin)

    except IntegrityError as e:

        await db.rollback()
        raise e
        
    return new_admin


async def get_all_admin(db: AsyncSession):

    result  = await db.execute((Admin))
    admins = result.scalars().all()

    if not admins:

        raise ValueError ("Admin not found")
    
    return admins

async def get_admin_by_id (db: AsyncSession, admin_id: int):

    result = await db.execute(
        select(Admin)
        .where(Admin.id == admin_id)
    )
    admin = result.scalar_one_or_none()

    if not admin:

        raise ValueError ("Admin not found")
    
    return admin

async def delete_admin_by_id(db: AsyncSession, admin_id: int):

    result = await db.execute(
        select(Admin)
        .where(Admin.id == admin_id)
    )

    admin = result.scalar_one_or_none()

    if not admin:

        raise ValueError ("Admin not found")
    
    try:

        await db.delete(admin)
        await db.commit()

    except SQLAlchemyError as e:

        await db.rollback()
        raise e
    
    return admin