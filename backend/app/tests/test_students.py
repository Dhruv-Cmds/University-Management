import pytest
import random


async def get_token(client):
    email = f"user{random.randint(1,100000)}@test.com"
    password = "123456"

    signup_response = await client.post(
        "/admin/signup",
        json={
            "email": email,
            "password": password,
            "role": "admin"
        }
    )

    print(signup_response.json())

    res = await client.post(
        "/admin/login",
        json={
            "email": email,
            "password": password
        }
    )

    print(res.json())

    assert res.status_code == 200

    return res.json()["access_token"]


@pytest.mark.asyncio
async def test_create_student(client):
    token = await get_token(client)

    response = await client.post(
        "/students/",
        json={
            "student_name": "John",
            "email": f"john{random.randint(1,100000)}@test.com",
            "phone_number": str(random.randint(1000000000, 9999999999)),
            "gender": "male"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print(response.json())

    assert response.status_code == 200