# user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    session_id = Column(String(100), nullable=True)
    reset_token = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
