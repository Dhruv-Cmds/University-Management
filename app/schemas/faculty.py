from pydantic import BaseModel, EmailStr

from app.schemas import NameStr, PhoneStr
from app.models import GenderEnum

# Shared base (reusable fields)
class FacultyBase(BaseModel):

    faculty_name: NameStr
    email: EmailStr
    phone_number: PhoneStr
    gender: GenderEnum

# For creating a new Faculty (request body) 
class FacultyCreate(FacultyBase):
   pass 

# For returning data from API (response)
class FacultyResponse(FacultyBase):

    id: int

    model_config = {
        "from_attributes": True
    }