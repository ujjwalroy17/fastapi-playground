from db import engine
from tables import  users, posts
from sqlalchemy import insert,select,asc,desc,func



# create users
def create_users(name: str,Email: str):
    with engine.connect() as conn:
        stmt = insert(users).values(name = name,Email = Email)
        conn.execute(stmt)
        conn.commit()
        
# Insert  or Create Post
def create_posts(user_id : int,title: str,content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id =  user_id,title = title,content = content)
        conn.execute(stmt)
        conn.commit()
        
# Get users ordered by name(A-Z)
def Get_users_ordered_by_name():
    with engine.connect() as conn:
        stmt = select(users).order_by(asc(users.c.name))
        result = conn.execute(stmt).fetchall()
        return result


# Get all posts ordered by latest 
def get_posts_latest_first():
    with engine.connect() as conn:
        stmt = select(posts).order_by(desc(posts.c.id))
        result = conn.execute(stmt).fetchall()
        return result
    
# Group  Posts  by user (Count how many posts  each user have)

def get_post_count_per_user():
    with engine.connect() as conn:
        stmt = select(
            posts.c.user_id,
            func.count(posts.c.id).label("Total post")
        ).group_by(posts.c.user_id)
        result = conn.execute(stmt).fetchall()
        return result