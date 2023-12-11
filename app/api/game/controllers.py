""" controllers.py """
from flask import Blueprint

game_bp = Blueprint("game", __name__)


@game_bp.route('/game/<game_id>/ready',
               methods=['POST'],
               strict_slashes=False)
def ready_game(game_id: str):
    return GameDTOHandler.ready(game_id=game_id)
