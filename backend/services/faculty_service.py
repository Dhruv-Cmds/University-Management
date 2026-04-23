from sqlalchemy.orm import Session
from backend.models import Faculty, Admin, Student
from backend.schemas import FacultyCreate

#  create faculty
def create_faculty(db:Session, faculty_data: FacultyCreate):

    existing_email_phone  = db.query(Faculty).filter(
        (Faculty.email == faculty_data.email) |
        (Faculty.phone_number == faculty_data.phone_number)).first()

    if existing_email_phone:

        raise ValueError ("Email already registered")
    
    existing_phone_email_student = db.query(Student).filter(
    (Student.phone_number == faculty_data.phone_number) |
    (Student.email == faculty_data.email)).first()

    if existing_phone_email_student:
        
        raise ValueError ("Phone number already used")
    
    existing_admin = db.query(Admin).filter(Admin.email == faculty_data.email).first()

    if existing_admin:
        raise ValueError("Email already used by a user")

    new_faculty = Faculty (

        faculty_name = faculty_data.faculty_name,
        email = faculty_data.email,
        phone_number = faculty_data.phone_number,
        gender = faculty_data.gender
    )

    try:

        db.add(new_faculty)

        db.commit()

        db.refresh(new_faculty)

    except Exception as e:

        db.rollback()
        raise e

    return new_faculty


#  get all faculty
def get_all_faculties(db:Session):

    return db.query(Faculty).all()


#  select specific id to check faculty
def get_faculty_by_id(db:Session, faculty_id: int):

    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    if not faculty:

        raise ValueError ("No faculty found")
    
    return faculty


# delete faculty
def delete_faculty (db:Session, faculty_id: int):

    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    if not faculty:

        raise ValueError ("No faculty found")
    
    try:
    
        db.delete(faculty)

        db.commit()

    except Exception as e:
        
        db.rollback()
        raise e
    
    return faculty