""" controllers.py """
from flask import Blueprint

from app.api.start.dto_handler import StartDTOHandler
from app.utils.error_handler import add_api_error_responses

start_bp = Blueprint("start", __name__)


@start_bp.route('/start/', methods=['POST'], strict_slashes=False)
@add_api_error_responses
def start_game():
    return StartDTOHandler.init_game()


@start_bp.route('/start/<game_id>', methods=['POST'], strict_slashes=False)
@add_api_error_responses
def join_game(game_id: str):
    return StartDTOHandler.join_game(game_id=game_id)
