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
