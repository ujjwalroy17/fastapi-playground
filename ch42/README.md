# FastAPI + SQLAlchemy ORM: Relationships

## Overview
In SQLAlchemy ORM, **relationships** define how database tables are connected.  
Instead of writing raw SQL joins, we can work with **Python objects** and let SQLAlchemy handle the linking.  

This makes it easy to represent **One-to-Many, One-to-One, and Many-to-Many** associations between models.

---

## 1. Unique Terms Explained

- **`ForeignKey`** → A constraint linking a column in one table to the `id` (or another column) in another table. Ensures referential integrity.  
  Example: `user_id = mapped_column(ForeignKey("users.id"))`

- **`relationship()`** → Defines how two models are related (one-to-many, one-to-one, many-to-many). It works with `ForeignKey`.  
  Example: `posts = relationship("Post", back_populates="user")`

- **`back_populates`** → Creates a **two-way relationship**. Both models can access each other.  
  Example:  
  - `User.posts` ↔ `Post.user`

- **`uselist`** → Defines whether the relationship should return a **list** (many) or a **single object** (one).  
  Example: `uselist=False` means **One-to-One**.

- **`cascade`** → Defines what happens when a parent object is deleted.  
  Example: `"all, delete"` ensures related child records are also deleted.

- **Association Table** → A separate table used in **Many-to-Many** relationships to connect two entities.  
  Example: `user_address_association` links users and addresses.

---

## 2. Types of Relationships

### 2.1 One-to-Many (User → Post)
- One **User** can have many **Posts**.  
- A `user_id` foreign key in `Post` links back to `User`.

```python
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship("User", back_populates="posts")
```
* If a user is deleted, all posts are deleted (cascade="all, delete").

### 2.2 One-to-One (User → Profile)
* One User has exactly one Profile.

* Achieved by setting ```uselist=False``` in ```relationship``` and ```unique=True``` in ```ForeignKey```.

```python
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete")

class Profile(Base):
    __tablename__ = "profile"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="profile")
```
* Each user can have only one profile.

### 2.3 Many-to-Many (User ↔ Address)
* A User can have many Addresses.

* An Address can belong to many Users.

* Requires an association table.

```python
user_address_association = Table(
    "user_address_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[list["Address"]] = relationship("Address", secondary=user_address_association, back_populates="users")

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    users: Mapped[list["User"]] = relationship("User", secondary=user_address_association, back_populates="address")
```
* The ```secondary=user_address_association``` tells SQLAlchemy to use the association table to link users and addresses.

## 3. Table Management
```python
def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)
```
* ```create_all()``` → Creates all tables in the database.

* ```drop_all()``` → Drops all tables (use carefully).

## 4. Quick Revision Points
* ForeignKey → Links one table’s column to another (enforces relationships).

* relationship() → ORM-level linking of models.

* back_populates → Enables two-way navigation.

* uselist=False → One-to-One relationship.

* cascade="all, delete" → Deletes related children with parent.

* Association Table → Used in Many-to-Many relationships.

* Relationship Types:

    * One-to-Many → User ↔ Posts

    * One-to-One → User ↔ Profile

    * Many-to-Many → User ↔ Address