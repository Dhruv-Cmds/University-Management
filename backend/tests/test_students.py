from fastapi.testclient import TestClient
from app.main import app
import random

client = TestClient(app)


def get_token():
    email = f"user{random.randint(1,100000)}@test.com"
    password = "123456"

    client.post("/auth/signup", json={
        "email": email,
        "password": password,
        "role": "admin"
    })

    res = client.post("/auth/login", json={
        "email": email,
        "password": password
    })

    return res.json()["access_token"]


def test_create_student():
    token = get_token()

    response = client.post(
        "/students/",
        json={
            "student_name": "John",
            "email": f"john{random.randint(1,100000)}@test.com",
            "phone_number": str(random.randint(1000000000, 9999999999)),
            "gender": "male"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200