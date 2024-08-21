from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from Engine.models.BaseModel import BaseModel

class Voter(BaseModel):
    """
    Represents a voter in the election system.

    Attributes:
        first_name: The first name of the voter.
        middle_name: The optional middle name of the voter.
        last_name: The last name of the voter.
        suffix: The optional suffix for the voter (e.g., "Jr.", "Sr.").
        id_number: An optional identifier for the voter.
        organization_id: The optional foreign key referencing the Organization.
        organization: A relationship to retrieve the parent Organization.
    """
    __tablename__ = 'voters'

    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    suffix = Column(String(255), nullable=True)
    id_number = Column(String(255), unique=True, nullable=True)

    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=True)

    # Adding relationship to get the parent Organization from Voter
    organization = relationship(
        'Organization', backref=backref('voters', lazy=True))

    def get_name(self) -> str:
        """
        Returns the full name of the voter in the format "First Middle Last Suffix".

        Returns:
            str: The full name of the voter.
        """
        middle_name: str = str(self.middle_name if self.middle_name else '')
        suffix: str = str(self.suffix if self.suffix else '')

        return f"{self.first_name} {middle_name} {self.last_name} {suffix}"

