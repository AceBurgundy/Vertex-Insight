from sqlalchemy import Column, String, DateTime
from Engine.models.BaseModel import BaseModel
from sqlalchemy.orm import relationship
from Engine.models.Vote import Vote

class Election(BaseModel):
    """
    Represents an election with voting sections.

    Attributes:
        title: The title of the election (e.g., "2024 School Presidential Elections").
        start_time: The datetime when voting starts.
        end_time: The datetime when voting ends.
        positions: A relationship to the Position model.
    """
    __tablename__ = 'elections'

    title = Column(String(255), nullable=False, unique=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    candidates = relationship('Candidate', foreign_keys='Candidate.election_id', order_by='desc(Candidate.created_at)')