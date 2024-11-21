#!/usr/bin/env python3
"""Auth class to interact with the authentication database.
"""
from db import DB
from user import User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound


def __init__(self) -> None:
    """
    Initialise the Auth instance

    Args:
        db (DB): An instance of DB class for database interaction.
    """
    self.__db = DB()


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


def register_user(self, email: str, password: str) -> User:
    """
    Register a new user with the provided email and password

    Args:
        email (str): Email of the user
        password (str): Password of the user

    Returns:
        User: Newly created user instance
    """
    try:
        self._db.find_user_by(email=email)
        raise ValueError(f"User {email} already exists.")
    except NoResultFound:
        # If no result is found, we can proceed to create a new user
        hashed_password = self._hash_password(password)
        return self._db.add_user(email=email, hashed_password=hashed_password)
