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


def test_create_course():
    token = get_token()

    course_name = f"Course_{random.randint(1,100000)}"

    response = client.post(
        "/courses/",
        json={"course_name": course_name},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["course_name"] == course_name


def test_get_courses():
    token = get_token()

    response = client.get(
        "/courses/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200