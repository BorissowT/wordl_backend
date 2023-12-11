""" game/model.py """

from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from app.api.user.model import User
from app.extensions import db


class Game(db.Model):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    game_id = Column(String)
    started_at = Column(Integer)
    rounds = Column(Integer)
    lap_time = Column(Integer)
    amount_users = Column(Integer)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship("User", primaryjoin=id==User.game_owner_id)
    users = relationship('User', backref='user',
                             primaryjoin=id==User.game_joined_id)
    words = Column(JSON, default=lambda: [])


class Word(db.Model):
    __tablename__ = "word"

    id = Column(Integer, primary_key=True)
    word = Column(String)
