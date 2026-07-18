import pytest
import random


@pytest.mark.asyncio
async def test_create_user_duplicate_email(client):
    email = f"user{random.randint(1,100000)}@test.com"

    first_response = await client.post(
        "/admin/signup",
        json={
            "email": email,
            "password": "123456",
            "role": "admin"
        }
    )

    print(first_response.json())

    response = await client.post(
        "/admin/signup",
        json={
            "email": email,
            "password": "123456",
            "role": "admin"
        }
    )

    print(response.json())

    assert response.status_code == 400