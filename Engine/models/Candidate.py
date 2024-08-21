from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from Engine.models.BaseModel import BaseModel

class Candidate(BaseModel):
    """
    Represents a candidate for a position in an election.

    Attributes:
        name: The name of the candidate.
        image_url: The URL of the candidate's image.
        position_id: The foreign key referencing the Position.
        id_number: An optional identifier for the candidate.
    """
    __tablename__ = 'candidates'

    name = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    position_id = Column(Integer, ForeignKey('positions.id'), nullable=False)
    id_number = Column(String(255), unique=True, nullable=True)

    # Adding relationship to get the parent Position from Candidate
    position = relationship('Position', backref=backref('candidates', lazy=True))
    voters = relationship('Voter', secondary='Vote', backref='candidates')

