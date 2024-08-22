from sqlalchemy import Column, String, ForeignKey, Integer, Text
from Engine.models.BaseModel import BaseModel
from Engine.models.Election import Election
from Engine.models.Vote import Vote
from sqlalchemy.orm import relationship
from typing import Optional

class Candidate(BaseModel):
    """
    Represents a candidate for a position in an election.

    Attributes:
        name: The name of the candidate.
        image_filename: The URL of the candidate's image.
        id_number: An optional identifier for the candidate.
        position_id: The foreign key referencing the Position.
        election_id: The foreign key referencing the Election.
    """
    __tablename__ = 'candidates'

    name = Column(String(255), nullable=False)
    image_filename = Column(Text, nullable=True)
    id_number = Column(String(255), unique=True, nullable=True)

    position_id = Column(Integer, ForeignKey('positions.id'), nullable=False)
    election_id = Column(Integer, ForeignKey('elections.id'), nullable=False)

    position = relationship('Position')
    election = relationship('Election')

    voters = relationship('Voter', secondary='vote', backref='candidates')
