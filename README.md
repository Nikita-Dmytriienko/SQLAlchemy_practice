# SQLAlchemy Practice

Small project to experiment with modern SQLAlchemy 2.x patterns, both sync and async.

### What's inside

- Declarative models with Annotated types
- Custom ENUM (Workload: parttime / fulltime)
- Automatic created_at / updated_at timestamps
- One-to-many relation (Worker → multiple Resumes)
- Core-style queries (Table + insert/select/update)
- ORM-style queries (session.add, scalars, joins, aggregations)
- Sync and async engines side-by-side (psycopg + asyncpg)
- Pydantic Settings for DB configuration
- Ruff + pre-commit for code quality and auto-formatting
- Example data insertion and average compensation grouping query

### Current status

Console scripts that create tables, insert sample data, and run various queries.  
No FastAPI endpoints.

### Setup & Installation

Project uses **uv** for fast dependency management (recommended).

```bash
# Install dependencies (runtime + dev)
uv sync --all-groups

# Install pre-commit hooks
pre-commit install
```
If you prefer pip:
```bash
# Runtime dependencies
pip install alembic asyncpg fastapi "psycopg[binary]" pydantic pydantic-settings sqlalchemy uvicorn

# Dev tools (ruff + pre-commit)
pip install ruff pre-commit

# Then install hooks
pre-commit install
```
To verify everything is set up correctly:
```bash
ruff check .
pre-commit run --all-files
```

### How to run
```bash
# Run the examples
python src/main.py
```
### Key files:

- src/models.py — models and annotations
- src/queries/orm.py — ORM examples (SyncORM / AsyncORM)
- src/queries/core.py — Core examples (SyncCore / AsyncCore)
- src/database.py — engines and Base setup
- src/config.py — settings via Pydantic

### MIT License