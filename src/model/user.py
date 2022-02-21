from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from model.base import Base, db

from typing import Union


class User(Base, db.Model):
    __tablename__ = "user"

    first_name = Column(String(128))
    last_name = Column(String(128))
    email = Column(String(128), unique=True)

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
