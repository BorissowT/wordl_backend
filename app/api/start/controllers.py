""" controllers.py """
from flask import Blueprint

from app.api.game.model import Game
from app.extensions import db

start_bp = Blueprint("start", __name__)


@start_bp.route('/start/', methods=['GET'], strict_slashes=False)
def start_game():

    game = Game(started_at=123)
    db.session.add(game)
    db.session.commit()
    return "started"
