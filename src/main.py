import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.queries.core import SyncCore, AsyncCore
from src.queries.orm import SyncORM, AsyncORM

SyncORM.create_tables()
SyncORM.insert_workers()
SyncORM.select_workers()
SyncORM.update_worker()

# SyncCore.create_tables()
# SyncCore.insert_workers()
# SyncCore.select_workers()
# SyncCore.update_worker()

# AsyncORM.create_tables()
# AsyncORM.insert_workers()
# AsyncORM.select_workers()
# AsyncORM.update_worker()

# AsyncCore.create_tables()
# AsyncCore.insert_workers()
# AsyncCore.select_workers()
# AsyncCore.update_worker()
