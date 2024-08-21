from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

from flask_admin.contrib.sqla import ModelView # type: ignore
from flask_admin import Admin # type: ignore

def setup_admin(app: Flask, database_instance: Optional[SQLAlchemy] = None):
    """
    Sets up the admin section of the app
    """
    # Create admin instance
    admin: Admin = Admin(app, name='Vertex Insight Admin Panel', template_mode='bootstrap3')

    # Models imported here to avoid circular import with BaseModels' import of db
    from .models import Election, Position, Candidate, Organization, Voter, Vote

    session = database_instance.session if database_instance else None

    # Add views
    admin.add_view(ModelView(Election, session))
    admin.add_view(ModelView(Position, session))
    admin.add_view(ModelView(Candidate, session))
    admin.add_view(ModelView(Organization, session))
    admin.add_view(ModelView(Voter, session))
    admin.add_view(ModelView(Vote, session))
