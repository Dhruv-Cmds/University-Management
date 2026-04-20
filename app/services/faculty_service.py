from sqlalchemy.orm import Session
from app.models import Faculty
from app.schemas import FacultyCreate

#  create student
def create_faculty(db:Session, faculty_data: FacultyCreate):

    existing_email  = db.query(Faculty).filter(
        Faculty.email == faculty_data.email).first()

    if existing_email:

        raise ValueError ("Email already registered")
    
    existing_phone = db.query(Faculty).filter(
        Faculty.phone_number == faculty_data.phone_number).first()

    if existing_phone:
        
        raise ValueError ("Phone number already used")

    faculty = Faculty (

        faculty_name = faculty_data.faculty_name,
        email = faculty_data.email,
        phone_number = faculty_data.phone_number,
        gender = faculty_data.gender
    )

    db.add(faculty)

    db.commit()

    db.refresh(faculty)

    return faculty


#  get all student
def get_all_faculties(db:Session):

    return db.query(Faculty).all()


#  select specific id to check student
def get_faculty_by_id(db:Session, faculty_id: int):

    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    if not faculty:

        raise ValueError ("No student found")
    
    return faculty


# delete student
def delete_faculty (db:Session, faculty_id: int):

    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    if not faculty:

        return None
    
    db.delete(faculty)

    db.commit()
    
    return faculty