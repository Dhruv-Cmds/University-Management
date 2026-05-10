import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from dotenv import load_dotenv
import os
import asyncio
from urllib.parse import quote_plus
import platform

import pytest_asyncio

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)

from sqlalchemy.orm import sessionmaker

from backend.db import Base
from backend.dependencies import get_db

from httpx import (
    AsyncClient,
    ASGITransport
)


# ===== ENV =====
env_path = (
    Path(__file__).resolve().parent.parent.parent
    / "docker"
    / ".env"
)

load_dotenv(env_path)


# ===== WINDOWS =====
if platform.system() == "Windows":

    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


# ===== DB =====
DB_USER = os.getenv("DB_USER")

DB_PASSWORD = quote_plus(
    os.getenv("DB_PASSWORD") or ""
)

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")

DB_PORT = os.getenv("DB_PORT", "3306")

DB_NAME = os.getenv("TEST_DB_NAME")


DATABASE_URL = (
    f"mysql+aiomysql://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

@pytest_asyncio.fixture(autouse=True)
async def cleanup_session(db_session):

    yield

    await db_session.rollback()


# ===== ENGINE =====
@pytest_asyncio.fixture(scope="session")
async def db_engine():

    from sqlalchemy.pool import NullPool

    engine = create_async_engine(
        DATABASE_URL,
        poolclass=NullPool,
        echo=False
    )

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.drop_all)

        await conn.run_sync(Base.metadata.create_all)

    yield engine



# ===== SESSION =====
@pytest_asyncio.fixture(scope="session")
async def db_session(db_engine):

    async_session = sessionmaker(
        bind=db_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False
    )

    session = async_session()

    yield session



# ===== CLIENT =====
@pytest_asyncio.fixture(scope="session")
async def client(db_session):

    from backend.main import app

    async def _get_db():

        try:
            yield db_session
        finally:
            await db_session.rollback()

    app.dependency_overrides[get_db] = _get_db

    app.state.limiter.enabled = False

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:

        yield ac

    app.dependency_overrides.clear()