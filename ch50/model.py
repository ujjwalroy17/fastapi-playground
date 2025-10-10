from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column
from sqlalchemy import  String,Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from db import engine

class Base(DeclarativeBase):
    pass

# User model/ User table
class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    email:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name} , email={self.email})>"
    

async def create_tables():
    async with engine.begin() as conn:
        await  conn.run_sync(Base.metadata.create_all)
    
async def drop_tables():
    async with engine.begin() as conn:
        await  conn.run_sync(Base.metadata.drop_all)
        