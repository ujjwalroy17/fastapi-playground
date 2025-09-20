# 📘 FastAPI + SQLAlchemy Core: Joins  

## 🔹 Overview  
Today’s focus was on learning how to perform **joins** in SQLAlchemy Core (not ORM).  
We worked with two tables:  
- `users` → stores user info.  
- `posts` → stores posts (with a foreign key to `users`).  

A **join** is used to combine rows from two or more tables based on a related column (in this case `posts.user_id = users.id`).  

---

## 🔹 Why Joins?  
- To **combine related data** from multiple tables.  
- To avoid storing duplicate/redundant information.  
- Example: Instead of storing the author name in every post, we store `user_id` in `posts` and then **join** with `users` whenever we need author details.  

---

## 🔹 Example: INNER JOIN (default in SQLAlchemy)  
We want to list all posts with their author’s name.  

```python
stmt = select(
    posts.c.id,
    posts.c.title,
    users.c.name.label("author_name")
).join(users, posts.c.user_id == users.c.id)
result = conn.execute(stmt).fetchall()
```
### What happens here?
* ```posts.c.id, posts.c.title``` → fetch post info.

* ```users.c.name.label("author_name")``` → fetch user name but rename the column to author_name.

* ```.join(users, posts.c.user_id == users.c.id)``` → performs INNER JOIN between posts and users.

### Equivalent SQL
```sql
SELECT posts.id, posts.title, users.name AS author_name
FROM posts
JOIN users ON posts.user_id = users.id;
```
## 🔹 Types of Joins in SQLAlchemy
By default, ```.join()``` creates an INNER JOIN.

But SQLAlchemy also supports other join types:

#### 1.INNER JOIN (default) → Returns only rows where there is a match in both tables.
```python
stmt = select(posts, users).join(users, posts.c.user_id == users.c.id)
```
#### 2.LEFT OUTER JOIN → Returns all rows from the left table, and matching rows from the right.

```python
stmt = select(posts, users).join(users, posts.c.user_id == users.c.id, isouter=True)
```
#### 3.RIGHT OUTER JOIN → Not directly supported in all dialects, but can be emulated by swapping tables.

#### 4.FULL OUTER JOIN → Supported in some databases using ```outerjoin()```.

##🔹 When to Use Joins
* INNER JOIN → When you want only data that exists in both tables.

* LEFT JOIN → When you want all records from ```posts``` even if no user exists (orphan data).

* RIGHT JOIN → When you want all users even if they have no posts.

* FULL JOIN → When you want all records, regardless of matching.

---