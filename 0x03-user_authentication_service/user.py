#!/usr/bin/env python3
"""User Base class module."""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


Base = declarative_base()


class User(Base):
    """Representation of a user."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        return f"<User: (id={self.id}>"
