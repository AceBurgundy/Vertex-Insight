from sqlalchemy import Column, ForeignKey, Integer
from Engine.models.BaseModel import BaseModel

class Vote(BaseModel):
    """
    Association table for many-to-many relationship between Voter and Candidate.

    Attributes:
        voter_id: The foreign key referencing the Voter.
        candidate_id: The foreign key referencing the Candidate.
        election_id: The foreign key referencing the Election.
    """
    __tablename__ = 'Votes'

    voter_id = Column(Integer, ForeignKey('voters.id'), primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'), primary_key=True)
    election_id = Column(Integer, ForeignKey('elections.id'), primary_key=True)
