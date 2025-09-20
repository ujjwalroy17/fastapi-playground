# FastAPI + SQLAlchemy ORM: Create Models

## Overview
This guide explains how to **create database models (tables) using SQLAlchemy ORM** in a FastAPI project.  
Models allow you to represent database tables as Python classes, making it easier to work with data in an object-oriented way.

---

## 1. Database Setup (`db.py`)

First, create a database connection and session:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///sqlite.db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
```
* ```echo=True``` logs all SQL statements executed (useful for debugging).

* ```expire_on_commit=False``` keeps objects "live" in memory after commit, so you can access attributes without reloading from the database.

* SQLite is built into Python; no extra installation needed.

## 2. Creating Models (models.py)

Models are Python classes that map to database tables.

## 2.1 Base Class
```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

* All models inherit from this Base class.

* Base provides metadata and mapping to SQL tables.

* `Base class`: a common superclass for all models; stores table metadata.

* `DeclarativeBase`: creates the base class, enabling Python classes to be mapped to database tables.

## 2.2 Note on Mapped and mapped_column

* Mapped: a type hint indicating this attribute is mapped to a database column.

* mapped_column(): defines the column type and constraints (e.g., primary key, nullable, unique).

* Mapping: linking class attributes to database columns, so Python objects correspond to table rows.

## 2.3 User Model
```python
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
```
### 2.4 Address Model
```python
class Address(Base):
    __tablename__ = "address"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(50), nullable=False)
    dist: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f"Address(id={self.id!r}, street={self.street!r})"
```
## 3. Creating and Dropping Tables
```python
# Create all tables
def create_tables():
    Base.metadata.create_all(engine)

# Drop all tables
def drop_tables():
    Base.metadata.drop_all(engine)
```
* ```create_all()``` creates tables in the database according to the models.

* ```drop_all()``` deletes all tables (use with caution).

* Both methods use the ```engine``` defined in ```db.py```.

## 4. Using in main.py
```python
from models import create_tables

create_tables()  # Creates tables in the database
```

* Running ```main.py``` will create the ```users and ```address``` tables in `sqlite.db` .

# 5. Key Points for Revision

* Models represent tables; class attributes represent columns.

* Use `Mapped` + `mapped_column` for defining typed columns.

* `primary_key`, `nullable`, and `unique` are important constraints.

* `Base.metadata.create_all(engine)` creates tables, `drop_all()` deletes tables.

* Use `echo=True` to log SQL statements and `expire_on_commit=False` to keep objects accessible after commit.

* Mapping links Python attributes to database columns so you can work with objects instead of raw SQL.