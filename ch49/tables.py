from sqlalchemy import MetaData,Column,Table,Integer,String
from db import engine


metadata = MetaData()


# User Table
users = Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=50), nullable=False),
    Column("Email",String,nullable=False,unique=True)
)
