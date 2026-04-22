from sqlalchemy.orm import Session
from app.models import Student, User, Faculty
from app.schemas import StudentCreate

#  create student
def create_student(db:Session, student_data: StudentCreate):

    existing_email_phone  = db.query(Student).filter(
        (Student.email == student_data.email) |
        (Student.phone_number == student_data.phone_number)).first()

    if existing_email_phone:

        raise ValueError("Student with this email or phone already exists")

    existing_faculty = db.query(Faculty)\
    .filter(Faculty.phone_number == student_data.phone_number)\
    .first()

    if existing_faculty:
        
        raise ValueError("Phone number already used by faculty")
    
    existing_user = db.query(User).filter(User.email == student_data.email).first()

    if existing_user:
        raise ValueError("Email already used by a user")
    

    new_student = Student (

        student_name = student_data.student_name,
        email = student_data.email,
        phone_number = student_data.phone_number,
        gender = student_data.gender
    )

    try:

        db.add(new_student)

        db.commit()

        db.refresh(new_student)
    
    except Exception as e:

        db.rollback()

        raise e

    return new_student


#  get all student
def get_all_students(db:Session):

    return db.query(Student).all()


#  select specific id to check student
def get_student_by_id(db:Session, student_id: int):

    student = db.query(Student).filter(
        Student.id == student_id).first()

    if not student:

        raise ValueError ("No student found")
    
    return student


# delete student
def delete_student (db:Session, student_id: int):

    student = db.query(Student).filter(
        Student.id == student_id).first()

    if not student:

        raise ValueError ("No student found")
    

    try:
    
        db.delete(student)

        db.commit()
    
    except Exception as e:

        db.rollback()
        raise e

    return student