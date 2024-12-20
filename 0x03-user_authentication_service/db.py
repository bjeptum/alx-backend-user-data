#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


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
        """Add and save new user to the database.
        """
        if not email or hashed_password:
            return
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the args"""
        if not kwargs:
            return InvalidRequestError
        try:
            # QUery User table with filters
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates user based on provided kwargs

        Args:
            user_id(int):The ID of user to be updated
            **kwargs: keyword arguments for user attributes to update
        """
        valid_attributes = {"email", "hashed_password"}

        # Find user by user_id
        user = self.find_user(id=user_id)

        # Update attributes
        for key, value in kwargs.items():
            if key not in allowed_attributes:
                raise ValueError
            setattr(user, key, value)

        # Commit changes to the database
        self._session.commit()
