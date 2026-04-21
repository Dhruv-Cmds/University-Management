from sqlalchemy import Column, Integer, String, Enum
from app.db import Base
import enum


class UserRole(str, enum.Enum):
    admin = "admin"
    student = "student"
    faculty = "faculty"


class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)  # will store hashed password

    role = Column(Enum(UserRole, name="user_role_enum"), nullable=False)