from src.database import sync_engine, async_session_factory, Base
from src.models import WorkersORM


def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


async def insert_data():
   async with async_session_factory() as session:
        worker_bobr = WorkersORM(username="Bobr")
        worker_zebra = WorkersORM(username="Zebra")
        session.add_all([worker_bobr, worker_zebra])
        await session.commit()