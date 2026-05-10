from backend.routes import courses, enrollements, faculty, students

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
from backend.db import engine, Base 

from backend.core import limiter
from backend.routes import auth

app = FastAPI(
    title="FastAPI College Management System",
    description=(
        "Secure college management API for admin authentication, "
        "student management, faculty management, course handling, "
        "and enrollment operations. "
        "Use the /admin/login endpoint to obtain authentication access "
        "for protected endpoints based on admin roles."
    ),
    version="1.0.0",
    lifespan=None,
    openapi_tags=[
        {
            "name": "Admin",
            "description": "Admin authentication and management endpoints."
        },
        {
            "name": "Courses",
            "description": "Manage courses including create, retrieve, and delete operations."
        },
        {
            "name": "Enrollments",
            "description": "Manage student enrollments in courses."
        },
        {
            "name": "Faculties",
            "description": "Faculty management endpoints."
        },
        {
            "name": "Students",
            "description": "Student management endpoints."
        }
    ]
)

@app.on_event("startup")
def on_startup():
    time.sleep(10) 
    Base.metadata.create_all(bind=engine)

app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(enrollements.router)
app.include_router(faculty.router)
app.include_router(students.router)