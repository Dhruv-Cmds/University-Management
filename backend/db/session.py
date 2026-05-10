from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)

from sqlalchemy.orm import sessionmaker

from urllib.parse import quote_plus
from dotenv import load_dotenv

import os

load_dotenv()

DB_USER = os.getenv("DB_USER")

DB_PASSWORD = quote_plus(
    os.getenv("DB_PASSWORD") or ""
)

DB_HOST = os.getenv("DB_HOST")

DB_PORT = os.getenv("DB_PORT", "3306")

DB_NAME = os.getenv("DB_NAME")


if not all([DB_USER, DB_HOST, DB_NAME]):

    raise ValueError(
        "Missing database environment variables"
    )


DATABASE_URL = (
    f"mysql+aiomysql://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_async_engine(
    DATABASE_URL,

    # validates dead connections automatically
    pool_pre_ping=True,

    # persistent pool
    pool_size=20,

    # temporary overflow connections
    max_overflow=30,

    # seconds to wait before timeout
    pool_timeout=30,

    # recycle stale mysql connections
    pool_recycle=1800,

    # set True only for debugging
    echo=False
)


AsyncSessionLocal = sessionmaker(
    bind=engine,

    class_=AsyncSession,

    expire_on_commit=False,

    autoflush=False,

    autocommit=False
)