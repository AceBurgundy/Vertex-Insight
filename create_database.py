from Engine import create_app
from flask import Flask
from Engine import db

app: Flask = create_app()

with app.app_context():
    from Engine.models import BaseModel, Organization, Admin, Election, Course, Position, Candidate, Voter, Vote
    db.create_all()
