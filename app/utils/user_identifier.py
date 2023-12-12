from flask import request

from app.api.user.model import User
from app.utils.custom_exceptions import ParameterException
from app.utils.token_generator import TokenGenerator


class UserIdentifier:

    @classmethod
    def get_user(cls):
        token = request.headers.get('Authorization', None)
        if token is None:
            raise ParameterException('Authorization param was not found')
        user_data = TokenGenerator.decode_token(token)
        user = User.query.get(user_data.get('user_id'))
        return user
