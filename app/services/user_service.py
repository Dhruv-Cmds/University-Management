from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate


def create_user(db: Session, user_data: UserCreate):
    existing = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing:
        raise ValueError("Email already registered")

    user = User(
        email=user_data.email,
        password=user_data.password,
        role=user_data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()