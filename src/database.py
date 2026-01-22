import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from src.config import settings

sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10
)


with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
    print(f"{res.first()=}")

async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")

asyncio.run(get_123())

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass

