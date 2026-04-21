import pytest
from app.db.session import SessionLocal
from app.models import User

@pytest.fixture(autouse=True)
def clean_db():
    db = SessionLocal()

    # clean ONLY users table (important for auth)
    db.query(User).delete()

    db.commit()
    db.close()