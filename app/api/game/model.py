""" game/model.py """
from app.extensions import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    started_at = db.Column(db.Integer)
