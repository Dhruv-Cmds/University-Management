from fastapi.testclient import TestClient
from backend.main import app
import random

client = TestClient(app)


def generate_user():
    email = f"user{random.randint(1,100000)}@test.com"
    password = "123456"
    return email, password


def test_signup():
    email, password = generate_user()

    response = client.post("/auth/signup", json={
        "email": email,
        "password": password,
        "role": "admin"
    })

    assert response.status_code == 200
    assert response.json()["email"] == email


def test_login():
    email, password = generate_user()

    client.post("/auth/signup", json={
        "email": email,
        "password": password,
        "role": "admin"
    })

    response = client.post("/auth/login", json={
        "email": email,
        "password": password
    })

    assert response.status_code == 200
    assert "access_token" in response.json()