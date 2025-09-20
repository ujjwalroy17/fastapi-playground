# 📘 FastAPI + SQLAlchemy Core: Order By & Group By  

## 🔹 Overview  
Today’s focus was on learning how to use **ORDER BY** and **GROUP BY** with **SQLAlchemy Core (not ORM)**.  
We worked with two tables:  
- `users` → stores user info.  
- `posts` → stores posts (with a foreign key to users).  

---

## 🔹 ORDER BY  
`ORDER BY` is used to **sort results** based on one or more columns.  

### Example 1: Get users ordered by name (A → Z)  
```python
stmt = select(users).order_by(asc(users.c.name))
```
* Uses `asc()` for ascending order.

* To get Z → A, use `desc()`.

###  Example 2: Get posts ordered by latest first
```python
stmt = select(posts).order_by(desc(posts.c.id))
```
* Sorting by id in descending order ensures latest posts appear first.

**Key Notes**:

* `asc()` → Ascending order `(default)`.

* `desc()` → Descending order.

* Can order by multiple columns if needed.

## 🔹 GROUP BY
`GROUP BY` is used to aggregate data (like counting, summing, averaging) grouped by a column.

✅ Example: Count posts per user
```python
stmt = select(
    posts.c.user_id,
    func.count(posts.c.id).label("Total post")
).group_by(posts.c.user_id)
Groups all posts by user_id.
```

* Uses ```func.count()``` to count how many posts each user has.

* ```.label("Total post")``` → gives a custom column name.

**Key Notes:**

* ```group_by()``` is always combined with ```aggregate functions (count, sum, avg, min, max)```.

* Without ```aggregate functions```, grouping doesn’t make sense.

----