from pydantic import BaseModel, EmailStr
from backend.models import AdminRole

from backend.schemas import PasswordStr

# shared fields
class AdminBase(BaseModel):
    email: EmailStr
    role: AdminRole

# create (incoming request)
class AdminCreate(AdminBase):
    password: PasswordStr


# login (separate, cleaner)
class AdminLogin(BaseModel):
    email: EmailStr
    password: str


# response (outgoing)
class AdminResponse(AdminBase):
    id: int

    model_config = {
        "from_attributes": True
    }