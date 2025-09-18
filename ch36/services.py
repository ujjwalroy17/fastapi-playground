from db import engine
from tables import  users, posts
from sqlalchemy import insert,select,update,delete



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
        
# Get single user by id
def get_user_by_id(user_id : int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)
        result = conn.execute(stmt).first()
        return result

# Get all users
def get_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).fetchall()
        return result
    
# Get Post by User
def get_posts_by_user(user_id : int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        result = conn.execute(stmt).fetchall()
        return result
    
# update user email
def update_user_email(user_id:int, new_email:str):
    with engine.connect() as conn:
        stmt = update(users).where(users.c.id == user_id).values(Email = new_email)
        conn.execute(stmt)
        conn.commit()
        
# delete Post
def delete_post(post_id:int):
    with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.id == post_id)
        conn.execute(stmt)
        conn.commit()   