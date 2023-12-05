""" dto_handler.py """
from flask import request

from app.api.game.model import Game
from app.api.start.schema import StartResponseSchema, StartRequestSchema
from app.api.user.model import User
from app.extensions import db


class StartDTOHandler:
    """This a data transfer abstraction layer. It's responsible for proper
     data validation, serialization and deserialization.

    """

    response_schema = StartResponseSchema()
    request_schema = StartRequestSchema()

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
            started_at="",
            rounds=start_data.get('rounds'),
            lap_time=start_data.get('lap_time'),
            amount_users=start_data.get('amount_users'),
            owner=user
        )
        db.session.add(game)
        db.session.commit()
        return jsonify({'inserted_id': encrypt_id(str(inserted_id))})
