from sqlalchemy.orm import Session
from backend.models import Admin
from backend.core.security import verify_password, create_access_token


def authenticate_admin(db: Session, email: str, password: str):

    # Password in DB is hashed (not plain text), so direct comparison won't work.
    # Instead of User.password == password, use verify_password()
    # which hashes the input and compares it securely.
    
    admin = db.query(Admin).filter(Admin.email == email).first()

    if not admin:
        raise ValueError("Invalid email or password")

    if not verify_password(password, admin.password):
        raise ValueError("Invalid email or password")

    return admin


def login_admin(db: Session, email: str, password: str):
    
    admin = authenticate_admin(db, email, password)

    if not admin:
        raise ValueError("Invalid email or password")

    token = create_access_token({
        "sub": str(admin.id),
        "role": admin.role.value
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }