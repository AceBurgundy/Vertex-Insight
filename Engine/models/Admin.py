from Engine.models.BaseModel import BaseModel
from sqlalchemy import Column, String
from flask_login import UserMixin # type: ignore

class Admin(BaseModel, UserMixin):
    """
    Represents an administrator with access to manage various aspects of the application.

    Attributes:
        username: The username of the admin.
        email: The email address of the admin.
        password_hash: The hashed password of the admin.
    """
    __tablename__ = 'admins'

    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    def __init__(self, username, email, password_hash) -> None:
        """
        Initialize an Admin instance.

        Args:
            username (str): The username of the admin.
            email (str): The email address of the admin.
            password_hash (str): The hashed password of the admin.
        """
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self) -> str:
        return f'<Admin {self.username}>'
