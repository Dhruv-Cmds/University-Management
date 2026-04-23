from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote_plus
from dotenv import load_dotenv

import os

load_dotenv()

DB_USER= os.getenv("DB_USER")
DB_PASSWORD=quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST= os.getenv("DB_HOST")
DB_NAME= os.getenv("DB_NAME")

if not all ([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
    raise ValueError("Database environment variables are not properly set")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

if not DATABASE_URL:
    raise ValueError ("DATABASE_URL is not set")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
    )

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)