from sqlalchemy.orm import  DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import String,ForeignKey, Table, Column,Integer
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
    


# Create Table
def create_tables():
    Base.metadata.create_all(engine)
    
# Drop Table
def drop_tables():
    Base.metadata.drop_all(engine)