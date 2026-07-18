import random


def generate_user():
    email = f"user{random.randint(1,100000)}@test.com"
    password = "123456"
    return email, password


async def test_signup(client):
    email, password = generate_user()

    response = await client.post(
        "/admin/signup",
        json={
            "email": email,
            "password": password,
            "role": "admin"
        }
    )

    assert response.status_code == 200
    assert response.json()["email"] == email


async def test_login(client):
    email, password = generate_user()

    await client.post(
        "/admin/signup",
        json={
            "email": email,
            "password": password,
            "role": "admin"
        }
    )

    response = await client.post(
        "/admin/login",
        json={
            "email": email,
            "password": password
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()