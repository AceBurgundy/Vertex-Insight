from Engine.models.BaseModel import BaseModel
from sqlalchemy import Column, String

class Organization(BaseModel):
    """
    Represents an organization where a student belongs.

    Attributes:
        name: The name of the organization (e.g., "College of Engineering and Technology").
    """
    __tablename__ = 'organizations'

    name = Column(String(255), nullable=False)

