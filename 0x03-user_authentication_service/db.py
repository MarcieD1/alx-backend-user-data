#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from typing import TypeVar

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

class CustomInvalidRequestError(Exception):
    pass

class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the Database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a User in the Database.
        """
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise CustomInvalidRequestError()

        user = self._session.query(User).filter_by(**kwargs).first()

        if user:
            return user
        raise NoResultFound()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        updating a user in the database
        """
        VALID_FIELDS = {'email', 'hashed_password', 'session_id', 'reset_token'}
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in VALID_FIELDS:
                raise ValueError(f"Invalid field: {k}")
            setattr(user, k, v)
        self._session.commit()

if __name__ == '__main__':
    my_db = DB()

    user = my_db.add_user("test@test.com", "PwdHashed")
    print(f"Added user with ID: {user.id}")

    try:
        find_user = my_db.find_user_by(email="test2@test.com")
        print(f"Found user with ID: {find_user.id}")
    except NoResultFound:
        print("User not found")

    try:
        find_user = my_db.find_user_by(no_email="test@test.com")
        print(f"Found user with ID: {find_user.id}")
    except CustomInvalidRequestError:
        print("Invalid request")

