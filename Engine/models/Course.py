from Engine.models.BaseModel import BaseModel
from sqlalchemy import Column, String

class Course(BaseModel):
    """
    Represents a course.

    Attributes:
        name: The name of the course
    """
    __tablename__ = 'courses'

    name = Column(String(255), unique=True, nullable=False)