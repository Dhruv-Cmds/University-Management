from sqlalchemy import Column, Integer, String, Enum
from backend.db import Base
import enum


class AdminRole(str, enum.Enum):
    admin = "admin"
    faculty = "faculty"


class Admin(Base):
    
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)  # will store hashed password

    role = Column(Enum(AdminRole, name="user_role_enum"), nullable=False)