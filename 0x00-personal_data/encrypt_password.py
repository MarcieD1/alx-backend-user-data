# encrypt_password.py
#!/usr/bin/env python3
"""
Module for encrypting passwords using bcrypt.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password with a salt.

    Args:
    password: The password to hash.

    Returns:
    A salted, hashed password as a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the provided password matches the hashed password.

    Args:
    hashed_password: The hashed password.
    password: The plain text password to verify.

    Returns:
    True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
