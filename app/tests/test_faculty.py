from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    res = client.post("/auth/login", json={
        "email": "test_auth@example.com",
        "password": "123456"
    })
    return res.json()["access_token"]


def test_create_faculty():
    token = get_token()

    response = client.post(
        "/faculties/",
        json={
            "faculty_name": "Dr Smith",
            "email": "smith@test.com",
            "phone_number": "9876543210",
            "gender": "male"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["faculty_name"] == "Dr Smith"