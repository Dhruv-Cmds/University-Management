from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import Enrollment
from backend.schemas import EnrollmentCreate

from fastapi import HTTPException

from sqlalchemy import select


#  create enrollment
async def create_enrollment(
        db: AsyncSession,
        enrollment_data: EnrollmentCreate
    ):

    result = await db.execute(
        select(Enrollment)
        .where(
            (Enrollment.student_id == enrollment_data.student_id) &
            (Enrollment.course_id == enrollment_data.course_id)
        )
    )

    existing = result.scalar_one_or_none()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Student is already enrolled in this course."
        )

    new_enrollment = Enrollment(
        student_id=enrollment_data.student_id,
        course_id=enrollment_data.course_id
    )

    try:

        db.add(new_enrollment)

        await db.commit()

        await db.refresh(new_enrollment)

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return new_enrollment


#  get all enrollment
async def get_all_enrollments(db: AsyncSession):

    result = await db.execute(
        select(Enrollment)
    )

    return result.scalars().all()


#  select specific id to check enrollment
async def get_enrollment_by_id(
        db: AsyncSession,
        enrollment_id: int
    ):

    result = await db.execute(
        select(Enrollment)
        .where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if not enrollment:

        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


# delete enrollment
async def delete_enrollment(
        db: AsyncSession,
        enrollment_id: int
    ):

    result = await db.execute(
        select(Enrollment)
        .where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if not enrollment:

        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    try:

        await db.delete(enrollment)

        await db.commit()

    except Exception:

        await db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    return enrollment