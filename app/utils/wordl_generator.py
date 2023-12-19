import random

import requests
from sqlalchemy import func

from app.api.game.model import Word
from app.extensions import db


class WordlWordsGenerator:

    @classmethod
    def return_5letter_word(cls) -> str:
        word = db.session.query(Word).order_by(func.random()).first()
        return word.word

    @classmethod
    def generate(cls, rounds):
        return [cls.return_5letter_word() for _ in range(rounds)]
