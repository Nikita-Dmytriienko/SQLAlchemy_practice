from typing import Annotated, ClassVar

from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings

sync_engine = create_engine(
    url=settings.database_url_psycopg, echo=True, pool_size=5, max_overflow=10
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg, echo=True, pool_size=5, max_overflow=10
)


with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
    print(f"{res.first()=}")


async def get_123():
    async with async_engine.connect() as connection:
        result = await connection.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{result.first()=}")


session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map: ClassVar = {str_256: String(256)}
