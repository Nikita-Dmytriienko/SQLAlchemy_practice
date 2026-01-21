from sqlalchemy import text
from src.database import async_engine, sync_engine
from src.models import metadata_obj


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")

async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        stmt = """INSERT INTO employers (username) VALUES
                ('Boba'),
                ('Roma'),
                ('Vitya');"""
        conn.execute(text(stmt))