from Engine.models.BaseModel import BaseModel
from sqlalchemy import Column, String

class Position(BaseModel):
    """
    Represents a position within an election (e.g., "President").

    Attributes:
        name: The name of the position.
    """
    __tablename__ = 'positions'

    name = Column(String(255), nullable=False, unique=True)
