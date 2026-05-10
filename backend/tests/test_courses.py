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
async def test_create_course(client):
    token = await get_token(client)

    course_name = f"Course_{random.randint(1,100000)}"

    response = await client.post(
        "/courses/",
        json={
            "course_name": course_name
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print(response.json())

    assert response.status_code == 200
    assert response.json()["course_name"] == course_name


@pytest.mark.asyncio
async def test_get_courses(client):
    token = await get_token(client)

    response = await client.get(
        "/courses/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print(response.json())

    assert response.status_code == 200