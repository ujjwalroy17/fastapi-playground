# 🚀 FastAPI Learning Log – Async SQLAlchemy Core with Alembic
 

## 🧩 Overview

In this session, I learned how to integrate **Async SQLAlchemy Core** with **Alembic** for database migrations in a FastAPI project.  
This setup enables asynchronous database operations and smooth schema migrations.

---

## ⚙️ Step 1: Virtual Environment Setup

```bash
D:\FastApi> D:\FastApi\ch47\venv\Scripts\activate.bat
(venv) D:\FastApi\ch49\venv\Scripts> deactivate
D:\FastApi> cd ch49
D:\FastApi\ch49> venv\Scripts\activate
```
## 📦 Step 2: Install Required Dependencies

Installed all required packages for Async SQLAlchemy Core and Alembic migration support:

```bash
Copy code
pip install alembic
pip install sqlalchemy[asyncio]
```
✅ Installed Packages
```ini
aiosqlite==0.21.0  
alembic==1.16.5  
greenlet==3.2.4  
Mako==1.3.10  
MarkupSafe==3.0.3  
SQLAlchemy==2.0.43  
typing_extensions==4.15.0  
```

## 🧠 Step 3: Initialize Alembic (Async Template)

Use Alembic’s async support for SQLAlchemy Core:

```bash
alembic init -t async alembic
```
### 📁 Generated folders & files:
```bash
Copy code
/alembic
/alembic/versions
alembic.ini
alembic/env.py
alembic/README
```
## 🗃️ Step 4: Configure Alembic
Edit **alembic.ini** and provide the correct SQLAlchemy database URL:

```ini
sqlalchemy.url = sqlite+aiosqlite:///./test.db
```
In **env.py**, ensure:

```python
from db import metadata
target_metadata = metadata
```
## 🧱 Step 5: Create Database Table (SQLAlchemy Core)
File: **tables.py**

```python
from sqlalchemy import MetaData, Column, Table, Integer, String
from db import engine

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("Email", String, nullable=False, unique=True)
)
```
## 🧩 Step 6: Generate and Run Migration
```bash
alembic revision --autogenerate -m "create users table"
```
#### 🖨️ Output:
```
bash
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
Generating D:\FastApi\ch49\alembic\versions\18a5d3b0e2b1_create_users_table.py ... done
```
## 🚀 Step 7: Apply the Migration
```bash
alembic upgrade head
```
#### 🖨️ Output:
```
INFO  [alembic.runtime.migration] Running upgrade  -> 18a5d3b0e2b1, create users table
```
**✅ Migration completed successfully!**

## 📘 Summary of Learnings

| 🧱 Step | 🏷️ Topic | 💡 Key Takeaways |
|:-------:|:----------|:----------------|
| 1 | Virtual Env Setup | Activated venv for isolated development. |
| 2 | Dependencies | Installed Async SQLAlchemy (`sqlalchemy[asyncio]`) + Alembic. |
| 3 | Alembic Init | Used `alembic init -t async alembic` for async template. |
| 4 | Config | Set `sqlalchemy.url` to use `sqlite+aiosqlite`. |
| 5 | Table Creation | Created `users` table using SQLAlchemy Core. |
| 6 | Migration | Used `alembic revision --autogenerate` to detect schema changes. |
| 7 | Upgrade | Applied migration with `alembic upgrade head`. |

## 🧾 Installation Recap (For Future Projects)
```bash
pip install sqlalchemy[asyncio]
pip install aiosqlite alembic Mako MarkupSafe typing_extensions greenlet
pip freeze > requirements.txt
```

