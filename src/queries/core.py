from sqlalchemy import text, insert, select
from src.database import async_engine, sync_engine
from src.models import metadata_obj, workers_table


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")

async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")

#Sync version
class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    def insert_workers():
        with sync_engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {"username": 'Vasya'},
                    {"username": 'Max'},
                ]
            )
            conn.execute(stmt)
            conn.commit()

    # @staticmethod
    # def select_workers():
    #     with session_factory() as session:
    #         query = select(WorkersOrm)
    #         result = session.execute(query)
    #         workers = result.scalars().all()

#Async  version
class AsyncCore:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(metadata_obj.drop_all)
            await conn.run_sync(metadata_obj.create_all)

        # @staticmethod
        # def create_tables():
        #     sync_engine.echo = False
        #     metadata_obj.drop_all(sync_engine)
        #     metadata_obj.create_all(sync_engine)
        #     sync_engine.echo = True