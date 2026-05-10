from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.models import Student, Admin, Faculty
from backend.schemas import StudentCreate


#  create student
async def create_student(db: AsyncSession, student_data: StudentCreate):

    result = await db.execute(
        select(Student).where(
            (Student.email == student_data.email) |
            (Student.phone_number == student_data.phone_number)
        )
    )

    existing_email_phone = result.scalar_one_or_none()

    if existing_email_phone:

        raise HTTPException(
            status_code=400,
            detail="Student with this email or phone already exists"
        )

    result = await db.execute(
        select(Faculty).where(
            (Faculty.phone_number == student_data.phone_number) |
            (Faculty.email == student_data.email)
        )
    )

    existing_faculty = result.scalar_one_or_none()

    if existing_faculty:

        raise HTTPException(
            status_code=400,
            detail="Phone number or email already used by faculty"
        )

    result = await db.execute(
        select(Admin).where(Admin.email == student_data.email)
    )

    existing_admin = result.scalar_one_or_none()

    if existing_admin:

        raise HTTPException(
            status_code=400,
            detail="Email already used by an admin"
        )

    new_student = Student(

        student_name=student_data.student_name,
        email=student_data.email,
        phone_number=student_data.phone_number,
        gender=student_data.gender
    )

    try:

        db.add(new_student)

        await db.commit()

        await db.refresh(new_student)

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return new_student


#  get all student
async def get_all_students(db: AsyncSession):

    result = await db.execute(
        select(Student)
    )

    return result.scalars().all()


#  select specific id to check student
async def get_student_by_id(db: AsyncSession, student_id: int):

    result = await db.execute(
        select(Student)
        .where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="No student found"
        )

    return student


# delete student
async def delete_student(db: AsyncSession, student_id: int):

    result = await db.execute(
        select(Student)
        .where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="No student found"
        )

    try:

        await db.delete(student)

        await db.commit()

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return student