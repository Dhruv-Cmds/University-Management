from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)

    enrollments = relationship(
        "Enrollment", 
        back_populates="course", 
        cascade="all, delete-orphan"
        )