from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.models import GenderEnum
from app.db import Base

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)

    gender = Column(Enum(GenderEnum, name="gender_enum"), nullable=False)

    enrollments = relationship(
        "Enrollment", 
        back_populates="student", 
        cascade="all, delete-orphan"
        )