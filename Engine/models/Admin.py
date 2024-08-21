from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String
from .BaseModel import BaseModel

class Admin(BaseModel):
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

    def __repr__(self):
        return f'<Admin {self.username}>'
