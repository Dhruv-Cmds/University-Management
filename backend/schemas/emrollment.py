from pydantic import BaseModel

# Shared base (reusable fields)
class EnrollmentBase(BaseModel):

    student_id: int
    course_id: int

# For creating a new Enrollment (request body) 
class EnrollmentCreate(EnrollmentBase):
    pass 

# For returning data from API (response)
class EnrollmentResponse(EnrollmentBase):

    id: int

    model_config = {
        "from_attributes": True
    }