from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your database connection URL here
DATABASE_URL = "sqlite:///users.db"

# Create a SQLAlchemy engine to connect to the database
engine = create_engine(DATABASE_URL, echo=True)

# Create a sessionmaker object for interacting with the database
Session = sessionmaker(bind=engine)

# Define a base class for declarative class definitions
Base = declarative_base()


# Define the User model class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    session_token = Column(String, default=None)
    reset_token = Column(String, default=None)


# Initialize the database schema
def init_db():
    Base.metadata.create_all(bind=engine)


# Define the DB class to interact with the database
class DB:
    def __init__(self):
        self.session = Session()
        # Initialize the database schema on instantiation
        init_db()

    def add_user(self, email: str, hashed_password: str):
        existing_user = self.get_user_by_email(email)
        if existing_user:
            raise ValueError(f"User with email '{email}' already exists.")

        new_user = User(email=email, hashed_password=hashed_password)
        self.session.add(new_user)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ValueError(f"User with email '{email}' already exists.")

        return new_user

    def get_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def update_user_session(self, user_id: int, session_token: str):
        user = self.session.query(User).filter(User.id == user_id).first()
        if user:
            user.session_token = session_token
            self.session.commit()
            return user
        return None

    def update_user_reset_token(self, email: str, reset_token: str):
        user = self.session.query(User).filter(User.email == email).first()
        if user:
            user.reset_token = reset_token
            self.session.commit()
            return user
        return None
