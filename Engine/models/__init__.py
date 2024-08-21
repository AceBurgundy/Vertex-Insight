"""
This module imports all the models and makes them available for use in the application.

Models:
- Election
- Position
- Candidate
- Organization
- Voter
- Vote
"""

from .Election import Election
from .Position import Position
from .Candidate import Candidate
from .Organization import Organization
from .Voter import Voter
from .Vote import Vote

__all__ = [
    'Election',
    'Position',
    'Candidate',
    'Organization',
    'Voter',
    'Vote'
]
