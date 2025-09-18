# 📘 FastAPI + SQLAlchemy Core: CRUD Operations

This document explains how to perform **CRUD operations** (Create, Read, Update, Delete) using **SQLAlchemy Core** in FastAPI.  
We use `insert()`, `select()`, `update()`, and `delete()` statements for database interaction.  

---

## 🔹 1. Database Setup
- **`MetaData()`** → Container for schema definitions.  
- **`Table`** → Defines tables manually.  
- **`engine`** → Connection to the database.  

```python
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

# Users Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("Email", String, nullable=False, unique=True)
)

# Posts Table (One-to-Many with Users)
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False)
)

# Create Tables
def create_tables():
    metadata.create_all(engine)

# Drop Tables
def drop_tables():
    metadata.drop_all(engine)

```
## 🔹 2. Database Connection

In every CRUD function, we use:

```python
with engine.connect() as conn:
```
#### ✅ What this does:
* engine.connect() → Opens a connection to the database.

* as conn → Gives us a connection object (conn) to run SQL queries.

* with ...: → This is a Python context manager. It ensures the connection is automatically closed when the block ends, even if an error occurs.

📌 Think of it like:
```python
with open("file.txt") as f:
    data = f.read()
# File automatically closed after block
```

## 🔹 3. CRUD Operations
### 3.1 Create (Insert)
```python
from sqlalchemy import insert

# Create User
def create_users(name: str, Email: str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, Email=Email)
        conn.execute(stmt)
        conn.commit()

# Create Post
def create_posts(user_id: int, title: str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content=content)
        conn.execute(stmt)
        conn.commit()
```
* ✅ Adds new data into the database.

### 3.2 Read (Select)
```python
from sqlalchemy import select

# Get single user by ID
def get_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)
        return conn.execute(stmt).first()

# Get all users
def get_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        return conn.execute(stmt).fetchall()

# Get posts by user
def get_posts_by_user(user_id: int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        return conn.execute(stmt).fetchall()
```
* ✅ Fetches data from tables using select().

### 3.3 Update
```python
from sqlalchemy import update

# Update user email
def update_user_email(user_id: int, new_email: str):
    with engine.connect() as conn:
        stmt = update(users).where(users.c.id == user_id).values(Email=new_email)
        conn.execute(stmt)
        conn.commit()
```
* ✅ Modifies existing data with update().

### 3.4 Delete
```python
from sqlalchemy import delete

# Delete post by ID
def delete_post(post_id: int):
    with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.id == post_id)
        conn.execute(stmt)
        conn.commit()
```
* ✅ Removes data from tables with delete().

## 🔹 4. Usage Example
```python
from tables import create_tables
from services import (
    create_users, create_posts, get_user_by_id,
    get_all_users, get_posts_by_user, update_user_email, delete_post
)

# Create tables
create_tables()

# Insert Data
create_users("Ujjwal", "ujjwal@gmail.com")
create_users("Raj", "raj@gmail.com")
create_posts(1, "Hello World", "This is Ujjwal's first post")
create_posts(2, "Raj's Post", "Hi from Raj!")

# Read Data
print(get_user_by_id(1))        # Get user by ID
print(get_all_users())          # Get all users
print(get_posts_by_user(2))     # Get Raj's posts

# Update Data
update_user_email(1, "ujjwal@newdomain.in")

# Delete Data
delete_post(2)
```
## 🔹 5. CRUD Summary Table

| Operation | SQLAlchemy Function | Example Function     |
|-----------|---------------------|----------------------|
| Create    | `insert()`          | `create_users()`     |
| Read      | `select()`          | `get_all_users()`    |
| Update    | `update()`          | `update_user_email()`|
| Delete    | `delete()`          | `delete_post()`      |

