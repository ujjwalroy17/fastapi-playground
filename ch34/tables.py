from db import engine
from sqlalchemy import MetaData,Table,Column,Integer,String

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

#We can create multiple tables as above

# Adress Table
address = Table(
    "address",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("street",String(length=50), nullable=False),
    Column("dist",String,nullable=False,unique=True),
    Column("country",String,nullable=False,unique=True)
)

# Create table in Database
def create_tables():
    metadata.create_all(engine)
    
# # Drop table from Database
# def drop_tables():
#     metadata.drop_all(engine)