from fastapi.testclient import TestClient
from app.main import app
import random

client = TestClient(app)


def test_create_user_duplicate_email():
    email = f"user{random.randint(1,100000)}@test.com"

    client.post("/auth/signup", json={
        "email": email,
        "password": "123456",
        "role": "admin"
    })

    response = client.post("/auth/signup", json={
        "email": email,
        "password": "123456",
        "role": "admin"
    })

    assert response.status_code == 400