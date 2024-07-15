# auth.py

from db import DB
from user import User  # Assuming User class is defined in user.py
from bcrypt import hashpw, gensalt

class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

def _hash_password(password: str) -> bytes:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def register_user(self, email: str, password: str) -> User:
        """Registers a new user in the database."""
        existing_user = self._db.get_user_by_email(email)
        if existing_user:
            raise ValueError(f"User {email} already exists.")

        hashed_password = self._hash_password(password)
        new_user = self._db.add_user(email, hashed_password.decode('utf-8'))
        return new_user
