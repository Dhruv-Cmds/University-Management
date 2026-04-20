from pydantic import BaseModel

from app.schemas import CourseStr

# Shared base (reusable fields)
class CourseBase(BaseModel):
    
    course_name = CourseStr

# For creating a new Course (request body) 
class CourseCreate(CourseBase):

    pass 

# For returning data from API (response)
class CourseResponse(CourseBase):

    id: int

    model_config = {
        "from_attributes": True
    }
    