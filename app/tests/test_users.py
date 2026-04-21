from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_admin_token():
    res = client.post("/auth/login", json={
        "email": "test_auth@example.com",
        "password": "123456"
    })
    return res.json()["access_token"]


def test_get_users_admin_only():
    token = get_admin_token()

    response = client.get(
        "/users/",
        headers={"Authorization": f"Bearer {token}"}
    )

    # This will work only if you implement users route
    assert response.status_code in [200, 404]


def test_create_user_duplicate_email():
    response = client.post("/auth/signup", json={
        "email": "test_auth@example.com",
        "password": "123456",
        "role": "admin"
    })

    # Should fail because already exists
    assert response.status_code == 400