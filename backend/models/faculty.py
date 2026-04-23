from sqlalchemy import Column, Integer, String, Enum

from app.models import GenderEnum
from app.db import Base

class Faculty(Base):

    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True, index=True)
    faculty_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, index=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)

    gender = Column(Enum(GenderEnum, name="gender_enum"), nullable=False)