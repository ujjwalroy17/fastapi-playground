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
    
    # One to Many : User to Post 
    posts:Mapped[list["Post"]] = relationship("Post",back_populates="users", cascade="all , delete")
    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name} , email={self.email})>"
    
# Post Model One to Many 
class Post(Base):
    __tablename__ = "posts"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    title: Mapped[str] = mapped_column(String,nullable=False)
    content:Mapped[str] = mapped_column(String,nullable=False)
    
    users:Mapped["User"] = relationship("User",back_populates="posts")
    
    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title} , content={self.content})>"


# Create Table
def create_tables():
    Base.metadata.create_all(engine)
    
# Drop Table
def drop_tables():
    Base.metadata.drop_all(engine)