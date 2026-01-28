import asyncio
import os
import sys

import uvicorn
from fastapi import FastAPI

from src.queries.core import AsyncCore, SyncCore
from src.queries.orm import AsyncORM, SyncORM

sys.path.insert(1, os.path.join(sys.path[0], ".."))


async def main():
    # ========== SYNC ==========
    # ORM
    if "--orm" in sys.argv and "--sync" in sys.argv:
        SyncORM.create_tables()
        SyncORM.insert_workers()
        SyncORM.select_workers()
        SyncORM.update_worker()

        SyncORM.insert_resumes()
        SyncORM.insert_additional_resumes()
        SyncORM.select_resumes_avg_compensation()

        # CORE
    elif "--core" in sys.argv and "--sync" in sys.argv:
        SyncCore.create_tables()
        SyncCore.insert_workers()
        SyncCore.select_workers()
        SyncCore.update_worker()

    # ========== ASYNC ==========
    # ORM
    if "--orm" in sys.argv and "--async" in sys.argv:
        AsyncORM.create_tables()
        AsyncORM.insert_workers()
        AsyncORM.select_workers()
        AsyncORM.update_worker()

    # CORE
    elif "--core" in sys.argv and "--async" in sys.argv:
        AsyncCore.create_tables()
        AsyncCore.insert_workers()
        AsyncCore.select_workers()
        AsyncCore.update_worker()


app = FastAPI()


if __name__ == "__main__":
    asyncio.run(main())
    if "--webserver" in sys.argv:
        uvicorn.run(
            app="src.main:app",
            reload=True,
        )
