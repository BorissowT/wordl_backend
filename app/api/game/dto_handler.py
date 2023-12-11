""" dto_handler.py """
import time

from app.api.game.model import Game
from app.extensions import db
from app.utils.custom_exceptions import NotFoundException, \
    NotEnoughPermissionsException
from app.utils.user_identifier import UserIdentifier


class GameDTOHandler:
    @classmethod
    def ready(cls, game_id):
        game: Game = (db.session.query(Game)
                      .filter(Game.game_id == game_id).first())
        if game is None:
            raise NotFoundException('the game not found')
        user = UserIdentifier.get_user()
        if game.owner != user:
            raise NotEnoughPermissionsException('you are not allowed to start'
                                                ' the game')
        current_time_struct = time.gmtime()

        # Convert the struct_time to a Unix timestamp
        unix_timestamp = int(time.mktime(current_time_struct))
        game.started_at = unix_timestamp
        db.session.commit()
