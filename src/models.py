from importlib.metadata import metadata

from sqlalchemy import Table, String, Integer, Column, MetaData
from sqlalchemy.orm import Mapped, mapped_column


metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
          Column("username", String),
)

