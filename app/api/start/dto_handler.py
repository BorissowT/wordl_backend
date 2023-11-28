""" dto_handler.py """
from flask import request

from app.api.start.schema import StartResponseSchema, StartRequestSchema
from app.api.user.model import User


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
        user = User(username=start_data.get('username'),
                    score=0,
                    skin=start_data.get('skin'))
        return jsonify({'inserted_id': encrypt_id(str(inserted_id))})