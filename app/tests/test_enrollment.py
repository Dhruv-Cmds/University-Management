from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    res = client.post("/auth/login", json={
        "email": "test_auth@example.com",
        "password": "123456"
    })
    return res.json()["access_token"]


def test_create_enrollment():
    token = get_token()

    response = client.post(
        "/enrollment/",
        json={
            "student_id": 1,
            "course_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200