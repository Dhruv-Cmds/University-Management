from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.models import Course
from backend.schemas import CourseCreate


#  create course
async def create_course(db: AsyncSession, course_data: CourseCreate):

    result = await db.execute(
        select(Course)
        .where(Course.course_name == course_data.course_name)
    )

    existing = result.scalar_one_or_none()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Course already exists"
        )

    new_course = Course(
        course_name=course_data.course_name
    )

    try:

        db.add(new_course)

        await db.commit()

        await db.refresh(new_course)

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return new_course


#  get all courses
async def get_all_courses(db: AsyncSession):

    result = await db.execute(
        select(Course)
    )

    return result.scalars().all()


#  select specific id to check course
async def get_course_by_id(db: AsyncSession, course_id: int):

    result = await db.execute(
        select(Course)
        .where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if not course:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


# delete course
async def delete_course(db: AsyncSession, course_id: int):

    result = await db.execute(
        select(Course)
        .where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if not course:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    try:

        await db.delete(course)

        await db.commit()

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return course