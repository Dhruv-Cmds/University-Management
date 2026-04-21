from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated
from app.models import UserRole

PasswordStr = Annotated[str, StringConstraints(min_length=6, max_length=128)]


# shared fields
class UserBase(BaseModel):
    email: EmailStr
    role: UserRole


# create (incoming request)
class UserCreate(UserBase):
    password: PasswordStr


# login (separate, cleaner)
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# response (outgoing)
class UserResponse(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }