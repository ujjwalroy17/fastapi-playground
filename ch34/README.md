# FastAPI Learning –  SQLAlchemy basics and DB table creation

## 1. Introduction

SQLAlchemy allows you to define database tables directly in Python using the **Core API**. You can create, update, or drop tables using Python code, without writing raw SQL statements.

**Key Points:**
- Tables are defined using the `Table` class.
- Columns are defined using the `Column` class along with data types like `Integer`, `String`, etc.
- Metadata is used to group and manage tables collectively.

---

## 2. Key Components

### 🔹 MetaData
- `MetaData` is a **container object that holds information about tables and schemas**.
- Think of it as a **directory or blueprint** of your database.
- It **does not store actual data**, but keeps track of table names, columns, constraints, and relationships.
- Required when creating or dropping tables.

**How it works:**
```python
from sqlalchemy import MetaData

metadata = MetaData()  # Create a metadata object
```
* Each table is associated with this metadata:

```
python
from sqlalchemy import Table, Column, Integer, String

users = Table(
    "users",
    metadata,  # links this table to the metadata container
    Column("id", Integer, primary_key=True),
    Column("name", String(50))
)
```
* `metadata.create_all(engine)` → creates all tables linked to metadata in the database.

* `metadata.drop_all(engine)` → removes all tables linked to metadata.

* **Analogy:**

* `MetaData` = table of contents for your database

* `Table` = each chapter

* `Engine` = printer that creates the tables in the database

---

### 🔹 Table
* Represents a database table.

* Requires:

    * Table name

    * Metadata object

    * List of columns

### 🔹 Column
* Represents a column in a table.

* Important parameters:

    * Integer, String(length) → Data type

    * primary_key=True → Marks column as primary key

    * nullable=False → Makes column mandatory

    * unique=True → Ensures column values are unique

## 3. Example: Creating Tables
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
    Column("Email", String, nullable=False, unique=True),
    Column("Phone_number", Integer, nullable=False, unique=True)
)

# Address Table
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String(length=50), nullable=False),
    Column("dist", String, nullable=False, unique=True),
    Column("country", String, nullable=False, unique=True)
)
```
### Notes:

* You can create multiple tables using the same MetaData object.

* Column names should avoid spaces (Phone_number is better than Phone number).

## 4. Creating and Dropping Tables
### Create Tables
```python
def create_tables():
    metadata.create_all(engine)
```
### Drop Tables (Optional)
```python
def drop_tables():
    metadata.drop_all(engine)
```
## 5. Best Practices & Tips
* Naming Conventions: Use snake_case for table and column names.

* Primary Keys: Always define a primary key for each table.

* Unique & Nullable Constraints: Use unique=True for fields like email or phone number.

* Multiple Tables: Use a single MetaData object to manage multiple tables efficiently.

* Future Expansion: For complex projects, consider using SQLAlchemy ORM for class-based table mapping.

## 6. Summary
* MetaData organizes table definitions.

* Table defines the table structure.

* Column defines the columns and constraints.

* create_all() generates tables in the database.

* drop_all() removes tables from the database.

**This is a foundational step for database operations in FastAPI applications.**