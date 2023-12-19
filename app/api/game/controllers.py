""" controllers.py """
from flask import Blueprint, jsonify, request

from app.api.game.dto_handler import GameDTOHandler
from app.utils.error_handler import add_api_error_responses

game_bp = Blueprint("game", __name__)


@game_bp.route('/game/<game_id>/ready',
               methods=['POST'],
               strict_slashes=False)
@add_api_error_responses
def ready_game(game_id: str):
    GameDTOHandler.ready(game_id=game_id)
    return jsonify('the game just started'), 200


@game_bp.route('/game/<game_id>/status',
               methods=['GET'],
               strict_slashes=False)
@add_api_error_responses
def get_status_game(game_id: str):
    return GameDTOHandler.get_status(game_id=game_id)


@game_bp.route('/game/<game_id>/scored',
               methods=['POST'],
               strict_slashes=False)
@add_api_error_responses
def score_user(game_id: str):
    GameDTOHandler.score_user(game_id=game_id)
    return jsonify("user score is updated"), 200
