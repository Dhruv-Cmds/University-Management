from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_signup():
    response = client.post("/auth/signup", json={
        "email": "test_auth@example.com",
        "password": "123456",
        "role": "admin"
    })

    assert response.status_code == 200
    assert response.json()["email"] == "test_auth@example.com"


def test_login():
    response = client.post("/auth/login", json={
        "email": "test_auth@example.com",
        "password": "123456"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()