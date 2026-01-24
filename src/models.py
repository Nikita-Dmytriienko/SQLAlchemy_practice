from typing import Optional

from sqlalchemy import Table, String, Integer, Column, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

import enum


class WorkersORM(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()


class Workload(enum.Enum):
    partime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    compensation: Mapped[Optional[int]] = mapped_column(nullable=True)
    workload: Mapped[Workload]
    worker: Mapped[id] = mapped_column(ForeignKey=("workers.id"))












metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
          Column("username", String),
)



