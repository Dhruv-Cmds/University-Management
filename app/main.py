from app.routes import courses, enrollements, faculty, students
from fastapi import FastAPI

from app.db import engine, Base 

from app.routes import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

app.include_router(courses.router)
app.include_router(enrollements.router)
app.include_router(faculty.router)
app.include_router(students.router)