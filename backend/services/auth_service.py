from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import Admin
from backend.core.security import verify_password, create_access_token


async def authenticate_admin(db: AsyncSession, email: str, password: str):

    # Password in DB is hashed (not plain text), so direct comparison won't work.
    # Instead of User.password == password, use verify_password()
    # which hashes the input and compares it securely.
    
    result = await db.execute(
        select(Admin)
        .where(Admin.email == email)
    )

    admin = result.scalar_one_or_none()

    if not admin:
        raise HTTPException (
            status_code=400,
            detail="Invalid email or password"
        )

    if not verify_password(password, admin.password):
        raise HTTPException (
            status_code=400,
            detail="Invalid email or password"
        )

    return admin


async def login_admin(db: AsyncSession, email: str, password: str):
    
    admin = await authenticate_admin(db, email, password)

    token = create_access_token({
        "sub": str(admin.id),
        "role": admin.role.value
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }