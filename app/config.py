"""config.py

Configuration class for setting different configurations for app.

"""
import os

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration."""
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('MONGO_URI')
    FLASK_ENV = config('FLASK_ENV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

