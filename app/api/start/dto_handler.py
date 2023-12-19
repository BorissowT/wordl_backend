""" dto_handler.py """
from flask import request

from app.api.game.model import Game
from app.api.start.schema import StartResponseSchema, StartRequestSchema, \
    JoinSchema
from app.api.user.model import User
from app.extensions import db
from app.utils.custom_exceptions import NotFoundException, \
    NotEnoughPermissionsException
from app.utils.game_id_generator import GameIdGenerator
from app.utils.token_generator import TokenGenerator


class StartDTOHandler:
    """This a data transfer abstraction layer. It's responsible for proper
     data validation, serialization and deserialization.

    """

    response_schema = StartResponseSchema()
    request_schema = StartRequestSchema()
    join_schema = JoinSchema()

    @classmethod
    def init_game(cls):
        """Validate input data and return encrypted id or raise validation
         error.

        :return: encrypted id
        """
        data = request.json
        start_data = cls.request_schema.load(data)
        # create user
        user: User = User(username=start_data.get('username'),
                          score=0,
                          skin=start_data.get('skin'))
        db.session.add(user)
        db.session.commit()
        # create game
        game = Game(
            started_at=0,
            game_id=GameIdGenerator.generate_url_token(),
            rounds=start_data.get('rounds'),
            lap_time=start_data.get('lap_time'),
            amount_users=start_data.get('amount_users')
        )
        db.session.add(game)
        db.session.commit()
        game.users.append(user)
        game.owner.append(user)
        game.owner_id = user.id
        db.session.commit()

        token = TokenGenerator.generate_token(user_id=user.id,
                                              username=user.username)
        # response schema
        response = cls.response_schema.dump({'game_id': game.game_id,
                                             'token': token})
        return response

    @classmethod
    def join_game(cls, game_id):
        data = request.json
        start_data = cls.join_schema.load(data)
        # create user
        user: User = User(username=start_data.get('username'),
                          score=0,
                          skin=start_data.get('skin'))
        db.session.add(user)
        db.session.commit()

        game = db.session.query(Game).filter(Game.game_id == game_id).first()
        if game is None:
            raise NotFoundException('the game not found')
        for registered_user in game.users:
            if registered_user.username == user.username:
                raise NotEnoughPermissionsException("User with this "
                                                    "username already in game")
        if len(game.users) == game.amount_users:
            raise NotEnoughPermissionsException("The game is full")

        db.session.commit()
        # generate token
        token = TokenGenerator.generate_token(user_id=user.id,
                                              username=user.username)
        response = cls.response_schema.dump({'game_id': game.game_id,
                                             'token': token})
        return response
