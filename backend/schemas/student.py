from pydantic import BaseModel, EmailStr

from backend.schemas import NameStr, PhoneStr
from backend.models import GenderEnum

# Shared base (reusable fields)
class StudentBase(BaseModel):

    student_name: NameStr
    email: EmailStr
    phone_number: PhoneStr
    gender: GenderEnum

# For creating a new student (request body) 
class StudentCreate(StudentBase):
   pass 

# For returning data from API (response)
class StudentResponse(StudentBase):

    id: int

    model_config = {
        "from_attributes": True
    }
