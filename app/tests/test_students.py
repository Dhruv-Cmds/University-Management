from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    res = client.post("/auth/login", json={
        "email": "test_auth@example.com",
        "password": "123456"
    })
    return res.json()["access_token"]


def test_create_student():
    token = get_token()

    response = client.post(
        "/students/",
        json={
            "student_name": "John",
            "email": "john@test.com",
            "phone_number": "1234567890",
            "gender": "male"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["student_name"] == "John"