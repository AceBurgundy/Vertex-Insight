from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from Engine.models.BaseModel import BaseModel

class Position(BaseModel):
    """
    Represents a position within an election (e.g., "President Candidates").

    Attributes:
        name: The name of the position.
        election_id: The foreign key referencing the Election.
        candidates: A relationship to the Candidate model.
        election: A relationship to retrieve the parent Election.
    """
    __tablename__ = 'positions'

    name = Column(String(255), nullable=False)
    election_id = Column(Integer, ForeignKey('elections.id'), nullable=False)
    candidates = relationship('Candidate', backref='position', lazy=True)

    # Adding relationship to get the parent Election from Position
    election = relationship('Election', backref=backref('positions', lazy=True))
