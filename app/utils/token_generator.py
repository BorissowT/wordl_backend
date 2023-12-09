import jwt
from app.config import Config


class TokenGenerator:
    secret_key = Config.SECRET_KEY

    @classmethod
    def generate_token(cls, user_id, username):
        token = jwt.encode({"user_id": user_id, "username": username},
                           cls.secret_key,
                           algorithm='HS256')
        return token

    def decode_token(self, token):
        try:
            decoded_data = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return decoded_data
        except jwt.ExpiredSignatureError:
            # Handle token expiration if needed
            print("Token has expired.")
            return None
        except jwt.InvalidTokenError:
            # Handle invalid token
            print("Invalid token.")
            return None
