from fastapi.testclient import TestClient
from backend.main import app
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


def test_create_enrollment():
    token = get_token()

    # create student
    student_res = client.post(
        "/students/",
        json={
            "student_name": "Test Student",
            "email": f"student{random.randint(1,100000)}@test.com",
            "phone_number": str(random.randint(1000000000, 9999999999)),
            "gender": "male"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert student_res.status_code == 200
    student_id = student_res.json()["id"]

    # create course (unique!)
    course_name = f"Course_{random.randint(1,100000)}"

    course_res = client.post(
        "/courses/",
        json={"course_name": course_name},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert course_res.status_code == 200
    course_id = course_res.json()["id"]

    # enroll
    response = client.post(
        "/enrollment/",
        json={
            "student_id": student_id,
            "course_id": course_id
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200