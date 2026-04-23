from pydantic import BaseModel, EmailStr

from app.schemas import NameStr, PhoneStr
from app.models import GenderEnum

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
