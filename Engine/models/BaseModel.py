from sqlalchemy import Column, Integer, DateTime as SQLAlchemyDateTime
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
    created_at = Column(SQLAlchemyDateTime, default=datetime.utcnow)

    @staticmethod
    def datetime_readable(datetime: datetime) -> str:
        """
        Convert a datetime object into a more readable string format.

        Args:
            datetime (DateTime): The datetime object to format.

        Returns:
            str: The formatted datetime string.
        """
        return datetime.strftime('%B %Y %I:%M%p')