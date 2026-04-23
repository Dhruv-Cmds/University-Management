from backend.routes import courses, enrollements, faculty, students

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.db import engine, Base 

from backend.routes import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(courses.router)
app.include_router(enrollements.router)
app.include_router(faculty.router)
app.include_router(students.router)