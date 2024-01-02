""" dto_handler.py """
import time

from flask import request

from app.api.game.model import Game
from app.api.game.schema import GameStatusResponseSchema
from app.api.user.model import User
from app.extensions import db
from app.utils.custom_exceptions import NotFoundException, \
    NotEnoughPermissionsException, TheGameHasNotStartedException
from app.utils.user_identifier import UserIdentifier
from app.utils.wordl_generator import WordlWordsGenerator


class GameDTOHandler:

    response_schema = GameStatusResponseSchema()

    @classmethod
    def ready(cls, game_id):
        game: Game = (db.session.query(Game)
                      .filter(Game.game_id == game_id).first())
        if game is None:
            raise NotFoundException('the game not found')
        user = UserIdentifier.get_user()
        if game.owner_id != user.id:
            raise NotEnoughPermissionsException('you are not allowed to start'
                                                ' the game')
        current_time_struct = time.gmtime()

        # Convert the struct_time to a Unix timestamp
        unix_timestamp = int(time.mktime(current_time_struct))
        game.started_at = unix_timestamp
        game.words = WordlWordsGenerator.generate(rounds=game.rounds)
        db.session.commit()

    @classmethod
    def get_status(cls, game_id):
        game: Game = (db.session.query(Game)
                      .filter(Game.game_id == game_id).first())
        if game is None:
            raise NotFoundException('the game not found')
        if game.started_at == 0:
            return TheGameHasNotStartedException()
        users_in_dict = [user.to_dict() for user in game.users]
        response = cls.response_schema.dump({
            'startedAt': game.started_at,
            'rounds': game.rounds,
            'words': game.words,
            'users': users_in_dict
        })
        return response

    @classmethod
    def score_user(cls, game_id):
        if game_id is None:
            raise NotFoundException('the game not found')
        data = request.json
        points = data.get('points')
        game: Game = (db.session.query(Game)
                      .filter(Game.game_id == game_id).first())
        user = UserIdentifier.get_user()
        if game is None:
            raise NotFoundException('the game not found')
        if not cls._check_if_user_in_game(user, game):
            raise NotEnoughPermissionsException('User with this username is '
                                                'not listed in game')
        if game.started_at == 0:
            raise TheGameHasNotStartedException()

        user.score += points
        db.session.commit()

    @classmethod
    def _check_if_user_in_game(cls, user: User, game: Game) -> bool:
        for registered_user in game.users:
            if registered_user.username == user.username:
                return True
        return False
