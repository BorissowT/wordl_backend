from datetime import datetime, timedelta

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from app.config import Config


class TokenGenerator:
    secret_key = Config.SECRET_KEY

    @classmethod
    def generate_token(cls, user_id, username):
        # Set expiration time to a distant future (e.g., 10 years)
        expiration_time = datetime.utcnow() + timedelta(days=3650)

        token = jwt.encode(
            {"user_id": user_id, "username": username, "exp": expiration_time},
            cls.secret_key,
            algorithm='HS256'
        )
        return token

    @classmethod
    def decode_token(cls, token):
        try:
            decoded_data = jwt.decode(token,
                                      cls.secret_key,
                                      algorithms='HS256')
            return decoded_data
        except jwt.ExpiredSignatureError as e:
            # Handle token expiration if needed
            raise ExpiredSignatureError(e)
        except jwt.InvalidTokenError as e:
            # Handle invalid token
            raise InvalidTokenError(e)
        except Exception as e:
            # Handle other JWT errors
            print(f"JWT decoding error: {str(e)}")
            return None
