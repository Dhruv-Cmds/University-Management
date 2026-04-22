from sqlalchemy.orm import Session
from app.models import User
from app.core.security import verify_password, create_access_token


def authenticate_user(db: Session, email: str, password: str):

    # Password in DB is hashed (not plain text), so direct comparison won't work.
    # Instead of User.password == password, use verify_password()
    # which hashes the input and compares it securely.
    
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user.password):
        raise ValueError("Invalid email or password")

    return user


def login_user(db: Session, email: str, password: str):
    user = authenticate_user(db, email, password)

    if not user:
        raise ValueError("Invalid email or password")

    token = create_access_token({
        "sub": str(user.id),
        "role": user.role.value
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }