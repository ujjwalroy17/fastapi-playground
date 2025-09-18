# 📘 FastAPI + SQLAlchemy Core: Relationships (One-to-One, One-to-Many, Many-to-Many)

This document explains how to implement different types of **database relationships** using **SQLAlchemy Core** (not ORM).  
We use `MetaData`, `Table`, `Column`, and `ForeignKey` to define schema and relationships.  

---

## 🔹 1. MetaData & Table Creation
- **`MetaData()`** → A container that stores table definitions.  
- **`Table`** → Defines database tables manually (unlike ORM models).  
- **`Column`** → Defines table fields with type and constraints.  
- **`ForeignKey`** → Creates relationships between tables.  

```python
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()
```
## 🔹 2. One-to-Many Relationship
📌 Definition: One record in Table A can be linked to multiple records in Table B.
👉 Example: A User can have many Posts.

```python
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone_number", Integer, nullable=False, unique=True),
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)

```
*  **Key Point**: If a user is deleted, their posts will also be deleted (ondelete="CASCADE").

## 🔹 3. One-to-One Relationship
📌 **Definition**: One record in Table A can be linked to only one record in Table B.

Example: A User has exactly one Profile.

```python
profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True),
    Column("bio", String, nullable=False),
    Column("address", String, nullable=False),
)
```
* **Key Point**: unique=True ensures only one profile exists per user.

##🔹 4. Many-to-Many Relationship
📌 **Definition**: A record in Table A can be linked to multiple records in Table B, and a record in Table B can also be linked to multiple records in Table A.

👉 Example:

A User can have multiple Addresses.

An Address can belong to multiple Users.

This type of relationship cannot be represented with just a `ForeignKey`.
Instead, we create a `junction (association)` table that acts as a bridge between the two tables.

*  ### Step 1: Create Main Tables
Here we define the Users and Addresses tables.

```python
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone_number", Integer, nullable=False, unique=True),
)

address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String, nullable=False),
    Column("country", String, nullable=False),
)
```
* ###Step 2: Create Association (Junction) Table
This table connects Users and Addresses.
Each row represents a unique User–Address relationship.

```python
user_address_association = Table(
    "user_address_association",
    metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),
)
```
#### Key Points for `Many-to-Many`:

1.Bridge Table → `user_address_association` acts as the `bridge` between users and address.

2.`Composite Primary Key` → (user_id, address_id) ensures that a user-address pair is always unique.

 * Example: If User1 is already linked to Address1, another duplicate row cannot be created.

3.`Bidirectional Relationship`→

   *  One user can have many addresses.

   * One address can belong to many users.

4.`Cascade Deletes` → If a user or address is deleted, related records in the association table are also removed.

#### xample Data Flow
* users:

    * Alice (id=1), Bob (id=2)

* address:

    * Delhi (id=1), Mumbai (id=2)

* user_address_association:

    * (user_id=1, address_id=1) → Alice ↔ Delhi

    * (user_id=1, address_id=2) → Alice ↔ Mumbai

    * (user_id=2, address_id=2) → Bob ↔ Mumbai

##🔹 5. Creating & Dropping Tables
```python
def create_tables():
    metadata.create_all(engine)

# def drop_tables():
#     metadata.drop_all(engine)
```
## 🔹 Summary of Relationships

| Relationship   | Example         | Implementation Trick                 |
|----------------|----------------|--------------------------------------|
| One-to-Many    | User → Posts   | Use `ForeignKey` without `unique`    |
| One-to-One     | User → Profile | Use `ForeignKey` with `unique=True`  |
| Many-to-Many   | User ↔ Address | Use a Junction (association) table   |




