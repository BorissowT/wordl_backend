""" game/model.py """

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

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
    owner = relationship("User")
    users = relationship("User", uselist=True)
