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
    Column("Email",String,nullable=False,unique=True),
        Column("Phone number",Integer,nullable=False,unique=True)

)

# One to Many Relations ------>

# # Posts Table
# posts = Table(
#     "posts",
#     metadata,
#     Column("id",Integer,primary_key=True),
#     Column("user_id",Integer, ForeignKey("users.id" , ondelete="CASCADE"),nullable=False),
#     Column("title",String,nullable=False),
#     Column("content",String,nullable=False)
# )

#<----------------->

# One to One Relations ------>

# Profile Table
profile = Table(
    "profile",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("user_id",Integer, ForeignKey("users.id" , ondelete="CASCADE"),nullable=False,unique=True),
    Column("Bio",String,nullable=False),
    Column("address",String,nullable=False),
    
)
 
#<------------->

# Many to Many relations --->

# Roles Table
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String, nullable=False),
    Column("country", String, nullable=False),
)

# Association Table (Linking Users and Roles)
user_address_association = Table(
    "user_address_association",
    metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),
)   

# <------------------>


# Create table in Database
def create_tables():
    metadata.create_all(engine)
    
# # Drop table from Database
# def drop_tables():
#     metadata.drop_all(engine)