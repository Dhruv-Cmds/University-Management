from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWSError, ExpiredSignatureError
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import User, UserRole
from app.core import SECRET_KEY, ALGORITHM

security = HTTPBearer()


def get_current_user(
                    credentials: HTTPAuthorizationCredentials = Depends(security),
                    db: Session = Depends(get_db)
                ):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except JWSError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def require_role(allowed_roles: list[UserRole]):

    def role_checker(current_user: User = Depends(get_current_user)):

        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        return current_user

    return role_checker