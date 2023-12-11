from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

from app.utils.wordl_generator import WordlWordsGenerator

db = SQLAlchemy()
Base = declarative_base()
wordl_generator = WordlWordsGenerator()
