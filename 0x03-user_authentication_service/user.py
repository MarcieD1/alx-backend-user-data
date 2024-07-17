#!/usr/bin/env python3
"""
Module to create user database
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """
    Creates table for user
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


if __name__== '__main__':
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}.".format(column, column.type))
