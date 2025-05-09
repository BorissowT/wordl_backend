import os

import requests
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.api.game.controllers import game_bp
from app.api.game.model import Word
from app.api.service.controller import service_bp
from app.api.start.controllers import start_bp
from app.config import Config
from app.extensions import db


def dump_words():
    url = "https://www.mit.edu/~ecprice/wordlist.100000"
    # TODO refacotr this function to another package
    response = requests.get(url)
    five_letter_words = [word.strip() for word in response.text.splitlines()
                         if len(word.strip()) == 5]
    for word in five_letter_words:
        model = Word(word=word)
        db.session.add(model)
    db.session.commit()


def create_app(config_class: Config = Config):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Create app
    app = Flask(__name__)

    # Set configuration variables
    app.config.from_object(config_class)
    app.secret_key = app.config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    app.url_map.strict_slashes = False

    db.init_app(app)
    # db = SQLAlchemy(app)

    if config_class.FLASK_ENV == "development":
        # init swagger

        SWAGGER_URL = '/api/docs'
        # URL for exposing Swagger UI (without trailing '/')
        API_URL = '/static/swagger.json'
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
            API_URL,
            config={  # Swagger UI config overrides
                'app_name': "Sidecar application"
            },

        )
        app.register_blueprint(swaggerui_blueprint)

        # register blueprints here

        app.register_blueprint(start_bp, url_prefix='/api/')
        app.register_blueprint(game_bp, url_prefix='/api/')
        app.register_blueprint(service_bp)

        # #create database
        # with app.app_context():
        #     db.create_all()
        #     dump_words()

    return app

# import os
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
