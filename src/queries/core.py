from sqlalchemy import text
from src.database import async_engine, engine
from src.models import metadata_obj



with engine.connect() as conn:
    res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
    print(f"{res.first()=}")

async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


def create_tables():
    metadata_obj.create_all(engine)