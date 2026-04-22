from sqlalchemy.orm import Session
from app.models import Enrollment
from app.schemas import EnrollmentCreate


#  create enrollment
def create_enrollment(
                    db:Session, 
                    enrollment_data: EnrollmentCreate
                    ):
    
    existing = db.query(Enrollment).filter(
            Enrollment.student_id == enrollment_data.student_id |
            Enrollment.course_id == enrollment_data.course_id).first()

    if existing:

         raise ValueError("Student already enrolled in this course")
    
    enrollment = Enrollment (
        student_id = enrollment_data.student_id,
        course_id = enrollment_data.course_id
    )

    try:

        db.add(enrollment)

        db.commit()

        db.refresh(enrollment)

    except Exception as e:

        db.rollback()
        raise e

    return enrollment
    

#  get all enrollment
def get_all_enrollments(db:Session):

    return db.query(Enrollment).all()


#  select specific id to check enrollment
def get_enrollment_by_id(
                        db:Session, 
                        enrollment_id:int
                        ):
    
    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id).first()

    if not enrollment:

        raise ValueError ("Enrollment not found")
    
    return enrollment

# delete enrollment
def delete_enrollment(
                db:Session, 
                enrollment_id:int
                ):
    
   enrollment = db.query(Enrollment).filter(
       Enrollment.id == enrollment_id).first() 

   if not enrollment:
       
       raise ValueError ("Enrollment not found")
   
   try:
        db.delete(enrollment)

        db.commit()

   except Exception as e:
       
       db.rollback()
       raise e

   return enrollment