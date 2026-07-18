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
async def test_create_enrollment(client):
    token = await get_token(client)

    # create student
    student_res = await client.post(
        "/students/",
        json={
            "student_name": "Test Student",
            "email": f"student{random.randint(1,100000)}@test.com",
            "phone_number": str(random.randint(1000000000, 9999999999)),
            "gender": "male"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print(student_res.json())

    assert student_res.status_code == 200
    student_id = student_res.json()["id"]

    # create course
    course_name = f"Course_{random.randint(1,100000)}"

    course_res = await client.post(
        "/courses/",
        json={
            "course_name": course_name
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print(course_res.json())

    assert course_res.status_code == 200
    course_id = course_res.json()["id"]

    # create enrollment
    response = await client.post(
        "/enrollments/",
        json={
            "student_id": student_id,
            "course_id": course_id
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print(response.json())

    assert response.status_code == 200