from sqlalchemy import text, insert
from src.database import async_engine, sync_engine, session_factory
from src.models import metadata_obj, workers_table, WorkersORM


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersORM(username="Bobr")
        worker_zebra = WorkersORM(username="Zebra")
        session.add_all([worker_bobr, worker_zebra])
        session.commit()
