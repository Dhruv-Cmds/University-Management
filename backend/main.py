from backend.routes import courses, enrollments, faculty, students

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from contextlib import asynccontextmanager

from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from backend.db import engine, Base
from backend.core import limiter
from backend.routes import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="FastAPI University Management System",
    description=(
        "Secure University management API for admin authentication, "
        "student management, faculty management, course handling, "
        "and enrollment operations. "
        "Use the /admin/login endpoint to obtain authentication access "
        "for protected endpoints based on admin roles."
    ),
    version="1.0.0",
    lifespan=lifespan,
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

app.state.limiter = limiter

# app.add_middleware(SlowAPIMiddleware)
import os

if os.getenv("TESTING") != "true":
    app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests, slow down"}
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(enrollments.router)
app.include_router(faculty.router)
app.include_router(students.router)