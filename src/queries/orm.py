from src.database import sync_engine, async_session_factory, Base
from src.models import WorkersORM


def create_tables():
    Base.metadata.drop_all(sync_engine)
    sync_engine.echo = True
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


async def insert_data():
    async with async_session_factory() as session:
        worker_sonya = WorkersORM(username="Sonya")
        worker_vika = WorkersORM(username="Vika")
        session.add_all([worker_sonya, worker_vika])
        await session.commit()
