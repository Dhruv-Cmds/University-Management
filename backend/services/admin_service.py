from sqlalchemy.orm import Session
from app.models import Admin
from app.schemas import AdminCreate

from app.core import hash_password


def create_admin(db: Session, admin_data: AdminCreate):
    existing = db.query(Admin).filter(
        Admin.email == admin_data.email
    ).first()

    if existing:
        raise ValueError("Email already registered")

    new_admin = Admin(
        email=admin_data.email,
        password=hash_password(admin_data.password),
        role=admin_data.role
    )

    try:

        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)

    except Exception as e:

        db.rollback()
        raise e
        
    return new_admin


def get_all_admin(db: Session):

    admin = db.query(Admin).all()

    if not admin:

        raise ValueError ("Admin not found")
    
    return admin

def get_admin_by_id (db: Session, admin_id: int):

    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:

        raise ValueError ("Admin not found")
    
    return admin

def delete_admin_by_id(db: Session, admin_id: int):

    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:

        raise ValueError ("Admin not found")
    
    try:

        db.delete(admin)
        db.commit()

    except Exception as e:

        db.rollback()
        raise e
    
    return admin