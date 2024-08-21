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

    title = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    positions = relationship('Position', backref='election', lazy=True)

    def Vote(self, candidate_id: int) -> int:
        """
        Returns the number of Vote a specific candidate has received in this election.

        Args:
            candidate_id: The ID of the candidate.

        Returns:
            int: The number of Vote the candidate has received.
        """
        # Query to count the number of Vote for the given candidate in this election
        return Vote.query.filter_by(election_id=self.id, candidate_id=candidate_id).count()
