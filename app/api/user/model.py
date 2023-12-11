""" user/model.py """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.extensions import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    score = Column(Integer)
    skin = Column(Integer)
    game_owner_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    game_joined_id = db.Column(db.Integer, db.ForeignKey('game.id'))

    def to_dict(self):
        return {'id': self.id,
                'username': self.username,
                'skin': self.skin,
                'score': self.score}
