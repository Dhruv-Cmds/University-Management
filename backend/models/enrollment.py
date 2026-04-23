from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Enrollment(Base):

    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")