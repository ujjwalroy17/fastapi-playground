# FastAPI Learning – SQLAlchemy Basics


## 1. Introduction to SQLAlchemy

### What is SQLAlchemy?
- A Python library that allows developers to interact with databases using Python code instead of raw SQL.
- Provides two main components:
  - **SQL Toolkit (Core):** Low-level SQL expression language.
  - **Object Relational Mapper (ORM):** Maps Python classes to database tables.

### Why use SQLAlchemy?
- You don’t always need to write raw SQL queries.
- Provides a Pythonic interface for schema creation, querying, and database management.
- Still gives you full control over SQL when needed.

---

## 2. Key Features of SQLAlchemy
✅ Maps Python classes to database tables (ORM).  
✅ Allows direct SQL expression construction (Core).  
✅ Supports multiple backends (SQLite, MySQL, PostgreSQL, etc.).  
✅ Provides tools for schema migrations, connection pooling, and transaction management.  

---

## 3. SQLAlchemy APIs

### 🔹 SQLAlchemy Core
- Lower-level API (close to SQL).
- Provides a schema-centric SQL expression language.

**Main Components:**
- **Engine:** The entry point; manages DB connection.  
- **Connection:** Represents a DBAPI connection.  
- **MetaData:** Holds table objects and schema.  
- **Table & Column:** Defines tables and their columns.  
- **SQL Expressions:** Build queries using Python objects.  

### 🔹 SQLAlchemy ORM
- Higher-level API (works with Python classes).
- Maps Python classes → Database tables.

**Main Components:**
- **Declarative Base:** Defines ORM models (class ↔ table).  
- **Session:** Handles persistence (add, delete, update, query).  
- **Query:** High-level interface for querying using Python syntax.  
- **Relationships:** Define one-to-many, many-to-many relationships.  

---

## 4. Installation

Install SQLAlchemy using pip:

```bash
pip install sqlalchemy
```
## 5. Creating the Database Engine
In SQLAlchemy, the engine is the starting point for any DB interaction.


```python
from sqlalchemy import create_engine

# Database URL format: dialect+driver://username:password@host:port/database
DATABASE_URL = "sqlite:///./sqlite.db"   # Using SQLite for simplicity

# Create engine
engine = create_engine(DATABASE_URL, echo=True)
```
**Notes:**

* sqlite:///./sqlite.db → SQLite database stored in local file sqlite.db.

* echo=True → Logs all SQL statements being executed (useful for debugging).