from passlib.context import CryptContext

from jose import jwt

from uuid import uuid4

from datetime import (
    datetime, 
    timedelta, 
    timezone
)

from .config import setting

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)

    now = datetime.now(timezone.utc)

    to_encode.update(
        {
            "iat": now,
            "nbf": now,  
            "exp": expire, 

            "iss": "delivery_api",
            "jti": str(uuid4())    
        }
    )

    token = jwt.encode(
        to_encode, 
        setting.SECRET_KEY, setting.ALGORITHM
    )

    
    return token