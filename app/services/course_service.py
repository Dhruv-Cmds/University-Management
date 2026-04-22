from sqlalchemy.orm import Session
from app.models import Course
from app.schemas import CourseCreate

#  create course
def create_course(db:Session, course_data: CourseCreate):

    existing = db.query(Course).filter(
        Course.course_name == course_data.course_name).first()
    
    if existing:

        raise ValueError ("Course already exists")

    course = Course(
        course_name = course_data.course_name
    )

    try:

        db.add(course)
        db.commit()
        db.refresh(course)

    except Exception as e:

        db.rollback()
        raise e

    return course

#  get all courses
def get_all_courses(db:Session):

    return db.query(Course).all()

#  select specific id to check course
def get_course_by_id(db:Session, course_id: int):

    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise ValueError ("Course not found")
    
    return course

# delete course
def delete_course(db:Session, course_id: int):

    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise ValueError ("Course not found")
    
    try:
    
        db.delete(course)

        db.commit()

    except Exception as e:
        
        db.rollback()
        raise e

    return course