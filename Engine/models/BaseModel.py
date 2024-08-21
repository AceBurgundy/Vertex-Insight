from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from Engine import db

class BaseModel(db.Model):  # type: ignore
    """
    Base model with common attributes for all models.

    Attributes:
        id: The unique identifier for the record.
        created_at: The timestamp when the record was created.
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
