import os
import sys

from src.queries.core import AsyncCore, SyncCore  # noqa: F401
from src.queries.orm import AsyncORM, SyncORM  # noqa: F401

sys.path.insert(1, os.path.join(sys.path[0], ".."))


SyncORM.create_tables()
SyncORM.insert_workers()
SyncORM.select_workers()
SyncORM.update_worker()

SyncORM.insert_resumes()
SyncORM.insert_additional_resumes()
SyncORM.select_resumes_avg_compensation()

# SyncCore.create_tables()
# SyncCore.insert_workers()
# SyncCore.select_workers()
# SyncCore.update_worker()
#
# AsyncORM.create_tables()
# AsyncORM.insert_workers()
# AsyncORM.select_workers()
# AsyncORM.update_worker()
#
# AsyncCore.create_tables()
# AsyncCore.insert_workers()
# AsyncCore.select_workers()
# AsyncCore.update_worker()
