""" controllers.py """
from flask import Blueprint

from app.api.start.dto_handler import StartDTOHandler

start_bp = Blueprint("start", __name__)


@start_bp.route('/start/', methods=['POST'], strict_slashes=False)
def start_game():
    return StartDTOHandler.init_game()
