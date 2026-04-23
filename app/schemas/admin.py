from pydantic import BaseModel, EmailStr
from app.models import AdminRole

from app.schemas import PasswordStr

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