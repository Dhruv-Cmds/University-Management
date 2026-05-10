from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.dependencies.db import get_db
from backend.models import Admin, AdminRole
from backend.models import Faculty
from backend.core import SECRET_KEY, ALGORITHM

security = HTTPBearer(auto_error=True)


async def get_current_admin(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: AsyncSession = Depends(get_db)
    ):
    
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("sub")
        role = payload.get("role")

        if not user_id or not role:
            raise HTTPException(status_code=401, detail="Invalid token")

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    model_map = {
        "admin": Admin,
        "faculty": Faculty
    }

    model = model_map.get(role)

    if not model:
        raise HTTPException(status_code=401, detail="Invalid role")

    result = await db.execute(
        select(model)
        .where(model.id == int(user_id))
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def require_role(allowed_roles: list[AdminRole]):

    async def role_checker(current_user: Admin = Depends(get_current_admin)):

        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        return current_user

    return role_checker