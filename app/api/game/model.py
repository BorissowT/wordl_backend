""" game/model.py """
from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db


class Game(db.Model):
    __tablename__ = "game"

    id = db.Column(db.Integer, primary_key=True)
    started_at = db.Column(db.Integer)
    rounds = db.Column(db.Integer)
    lap_time = db.Column(db.Integer)
    amount_users = db.Column(db.Integer)
    owner_id: Mapped[int] = mapped_column()
    users: Mapped[Optional["User"]] = relationship()
