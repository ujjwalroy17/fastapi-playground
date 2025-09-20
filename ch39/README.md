# FastAPI Learning – Raw SQL with SQLAlchemy Core

This note covers how to use **Raw SQL** queries inside FastAPI using **SQLAlchemy Core** (not ORM).  
We directly write SQL queries (`INSERT`, `SELECT`, etc.) but still use SQLAlchemy’s `engine` for execution.

---



## 1. SQLAlchemy Core (Not ORM)
- **Core** works with tables and SQL statements directly.
- No need to define Python classes like in ORM.
- We explicitly define `Table`, `Column`, `MetaData` etc.

---

## 2. Defining Tables (`tables.py`)
```python
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

# User Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True)  # lowercase 'email' is preferred
)

# Create tables in the database
def create_tables():
    metadata.create_all(engine)
```
#### 🔹 Here:

* ```MetaData()``` is a container of table objects.

* ```users``` defines a ```users``` table with ```id```, ```name```, and ```email```.

* ```create_all(engine)``` actually creates the table in the DB.

## 3. Raw SQL Queries with SQLAlchemy (```services.py```)
SQLAlchemy provides the ```text()``` method to write Raw SQL queries safely.

### (a) Insert Query
```python
from db import engine
from sqlalchemy import text

def raw_sql_insert():
    with engine.connect() as conn:
        stmt = text("""
            INSERT INTO users (name, email)
            VALUES (:name, :email)
        """)
        conn.execute(stmt, {"name": "ujjwal", "email": "ujjwal@gmail.com"})
        conn.commit()
```
* Uses named parameters (```:name```, ```:email```) → helps prevent SQL injection.
* ```conn.commit()``` is required to save the data.

(b) Select Query
```python
def raw_sql_select():
    with engine.connect() as conn:
        stmt = text("""
            SELECT * FROM users WHERE email = :email
        """)
        result = conn.execute(stmt, {"email": "ujjwal@gmail.com"}).first()
        return result
```
* ```first()``` → returns the first matching row.
* Returns a tuple like (```id```, ```name```, ```email```).

4. Main File (```main.py```)
```python
from tables import create_tables
from services import *

create_tables()

raw_sql_insert()  

print(raw_sql_select())
```
* First creates the table.

* Inserts sample data (if ```raw_sql_insert()``` is called).

* Runs ```raw_sql_select()``` to fetch a row.

## Advantages of Using text() for Raw SQL
* Flexible: Write any SQL query directly.

* Safe: Named parameters (```:param```) prevent ```SQL injection```.

* Works alongside Core/ORM queries.