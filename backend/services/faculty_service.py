from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.models import Faculty, Admin, Student
from backend.schemas import FacultyCreate


#  create faculty
async def create_faculty(db: AsyncSession, faculty_data: FacultyCreate):

    result = await db.execute(
        select(Faculty).where(
            (Faculty.email == faculty_data.email) |
            (Faculty.phone_number == faculty_data.phone_number)
        )
    )

    existing_email_phone = result.scalar_one_or_none()

    if existing_email_phone:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    result = await db.execute(
        select(Student).where(
            (Student.phone_number == faculty_data.phone_number) |
            (Student.email == faculty_data.email)
        )
    )

    existing_phone_email_student = result.scalar_one_or_none()

    if existing_phone_email_student:

        raise HTTPException(
            status_code=400,
            detail="Phone number already used"
        )

    result = await db.execute(
        select(Admin).where(Admin.email == faculty_data.email)
    )

    existing_admin = result.scalar_one_or_none()

    if existing_admin:

        raise HTTPException(
            status_code=400,
            detail="Email already used by a user"
        )

    new_faculty = Faculty(
        faculty_name=faculty_data.faculty_name,
        email=faculty_data.email,
        phone_number=faculty_data.phone_number,
        gender=faculty_data.gender
    )

    try:

        db.add(new_faculty)

        await db.commit()

        await db.refresh(new_faculty)

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return new_faculty


#  get all faculty
async def get_all_faculties(db: AsyncSession):

    result = await db.execute(
        select(Faculty)
    )

    return result.scalars().all()


#  select specific id to check faculty
async def get_faculty_by_id(db: AsyncSession, faculty_id: int):

    result = await db.execute(
        select(Faculty)
        .where(Faculty.id == faculty_id)
    )

    faculty = result.scalar_one_or_none()

    if not faculty:

        raise HTTPException(
            status_code=404,
            detail="No faculty found"
        )

    return faculty


# delete faculty
async def delete_faculty(db: AsyncSession, faculty_id: int):

    result = await db.execute(
        select(Faculty)
        .where(Faculty.id == faculty_id)
    )

    faculty = result.scalar_one_or_none()

    if not faculty:

        raise HTTPException(
            status_code=404,
            detail="No faculty found"
        )

    try:

        await db.delete(faculty)

        await db.commit()

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return faculty