# FastAPI + SQLAlchemy ORM Setup

## Overview
This guide explains how to **install and set up SQLAlchemy ORM** in a FastAPI project.  
SQLAlchemy is a popular Python ORM (Object Relational Mapper) that allows you to interact with databases using Python objects instead of raw SQL queries.

---

## 1. Installation

Install SQLAlchemy:

```bash
pip install sqlalchemy
```
**Note**: ```SQLite``` comes ```built into Python```, so you do not need to install it separately.

You only need to install a driver if you use another database like PostgreSQL or MySQL.

```bash
# For PostgreSQL
pip install psycopg2
```
## 2. Database URL
The database URL tells SQLAlchemy which database to connect to. Format:

```bash
dialect+driver://username:password@host:port/database
```
Examples:

* SQLite: ```"sqlite:///sqlite.db"``` (local file-based database)

* PostgreSQL: ```"postgresql+psycopg2://user:password@localhost/dbname"```

## 3. Create SQLAlchemy Engine
The engine is the starting point for any SQLAlchemy application. It manages the connection pool and database dialect.

```python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///sqlite.db"

engine = create_engine(DATABASE_URL, echo=True)
```
* ```echo=True``` logs all SQL statements executed, useful for debugging.

## 4. Create a Session
Sessions allow you to interact with the database in a transactional way. Use sessionmaker to create session objects.

```python
from sqlalchemy.orm import sessionmaker
```
* ```SessionLocal``` = sessionmaker(bind=engine, expire_on_commit=False)
* ```bind=engine``` tells the session which database to use.

* ```expire_on_commit=False``` prevents SQLAlchemy from expiring objects after commit, making it easier to access them after saving.

Explanation:

Default behavior (expire_on_commit=True): After ```db.commit()```, SQLAlchemy marks objects as expired. Accessing attributes reloads them from the database.

With ```(expire_on_commit=False)```: Objects remain "live" in memory after commit. You can access their attributes directly without querying the database again.