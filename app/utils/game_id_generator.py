import secrets


class GameIdGenerator:
    @classmethod
    def generate_url_token(cls, length=10):
        token = secrets.token_urlsafe(length)[:length]
        return token
