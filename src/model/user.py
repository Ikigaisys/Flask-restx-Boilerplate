from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from model.base import Base, db

from typing import Union


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    @classmethod
    def get_by_email(cls, email: str) -> Union["User", None]:
        """
        Get user by email

        Args:
            email: user email

        Returns:
            User
        """
        row = db.session.query(cls).filter(User.email == email).first()
        return row
