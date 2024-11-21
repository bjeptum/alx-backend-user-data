#!/usr/bin/env python3
"""Authentication module to handle user operations
"""
from db import DB
import bcrypt


def __init__(self, db: DB) -> None:
    """
    Initialise the Auth instance

    Args:
        db (DB): An instance of DB class for database interaction.
    """
    self.__db = db


def _hash_password(self, password: str) -> bytes:
    """
    Hash a password using bcrypt

    Args:
        password (str): The password to hash

    Returns:
        bytes: The salted hash of the password
    """
    # Convert to bytes
    password_bytes = password.encode('utf8')

    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed
