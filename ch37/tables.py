# Sqlalchemy core approach this not ORM

from db import engine
from sqlalchemy import MetaData,Table,Column,Integer,String,ForeignKey

metadata = MetaData()

# User Table
users = Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=50), nullable=False),
    Column("Email",String,nullable=False,unique=True)
)

# One to Many Relations ------>

# Posts Table
posts = Table(
    "posts",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("user_id",Integer, ForeignKey("users.id" , ondelete="CASCADE"),nullable=False),
    Column("title",String,nullable=False),
    Column("content",String,nullable=False)
)

#<----------------->



# Create table in Database
def create_tables():
    metadata.create_all(engine)
    
# # Drop table from Database
# def drop_tables():
#     metadata.drop_all(engine)