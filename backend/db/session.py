from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
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
    raise ValueError("Missing database environment variables")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=30,
    pool_timeout=30,
    echo=False
    )


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)