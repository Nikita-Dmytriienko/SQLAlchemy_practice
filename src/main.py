import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.queries.core import SyncCore
from src.queries.orm import SyncORM, AsyncORM

SyncORM.create_tables()
SyncORM.insert_workers()
#SyncCore.create_tables()

#AsyncORM.create_tables()
#AsyncORM.insert_workers()
#AsyncCore.create_tables()

SyncCore.select_workers()
SyncCore.update_workers()

# asyncio.run(insert_data())
