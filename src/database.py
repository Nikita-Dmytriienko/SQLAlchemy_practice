from sqlalchemy import URL, create_engine, text

from src.config import settings

engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)


with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res=}")