# FastAPI + SQLAlchemy ORM: CRUD Operations & ORDER BY

## Overview
This chapter focuses on how to perform **CRUD operations** (Create, Read, Update, Delete) and **ordering data** using SQLAlchemy ORM with FastAPI.  
It explains how to interact with the database via models, sessions, and relationships.

---

## 1. Project File Structure
FastAPI Project/
│
├── db.py
├── models.py
├── services.py
└── main.py

python
Copy code

---

## 2. Core Concepts

### 2.1 Declarative Base
`Base` is the base class for all SQLAlchemy models.  
It comes from `DeclarativeBase` and is used to define ORM-mapped classes. Every model should inherit from it.

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```
### 2.2 Mapped & Mapping Concepts
| Term           | Meaning                                                      |
|----------------|--------------------------------------------------------------|
| Mapped         | Represents a typed column or relationship in a model class. |
| mapped_column()| Defines a database column with type and constraints.       |
| Mapping        | The process of linking Python classes (models) with database tables. |


Example:

```python
id: Mapped[int] = mapped_column(primary_key=True)
```
## 3. Models (models.py)
### 3.1 User Model
```python
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # One-to-Many relationship with Post
    posts: Mapped[list["Post"]] = relationship(
        "Post", back_populates="users", cascade="all, delete"
    )

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
```
### 3.2 Post Model
```python
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, content={self.content})>"
```
## 4. CRUD Operations (services.py)
### 4.1 Create
```python
def create_user(name: str, email: str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def create_post(user_id: int, title: str, content: str):
    with SessionLocal() as session:
        post = Post(user_id=user_id, title=title, content=content)
        session.add(post)
        session.commit()
```
### 4.2 Read
```python
def get_user_by_id(user_id: int):
    with SessionLocal() as session:
        user = session.get_one(User, user_id)
        return user

def get_all_users():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users
```
### 4.3 Update
```python
def update_user_email(user_id: int, new_email: str):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()
        return user
```
### 4.4 Delete
```python
def delete_post(post_id: int):
    with SessionLocal() as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()
```
## 5. Order By
Sort results in ascending order using order_by():

```python
from sqlalchemy import asc

def get_users_ordered_by_name():
    with SessionLocal() as session:
        stmt = select(User).order_by(asc(User.name))
        users = session.scalars(stmt).all()
        return users
```
## 6. Additional Notes
* ```SessionLocal()``` handles database transactions safely using context manager (```with```).

* ```session.commit()``` permanently saves changes.

* ```session.refresh()``` updates the object with new database data.

* ```relationship()``` helps in linking tables logically (One-to-Many, Many-to-One).

* Use ```.scalars(stmt)``` to get pure model objects instead of row tuples.

