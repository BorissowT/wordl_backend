""" schema.py """

"""apartment_configs/schema.py

This package contains schema class for serialization and deserialization of
incoming and outgoing responses.

"""
from marshmallow import Schema, fields, validates, ValidationError


class StartResponseSchema(Schema):

    game_id = fields.Str(dumps_only=True)
    token = fields.Str(dumps_only=True)


class JoinSchema(Schema):
    username = fields.Str(required=True)
    skin = fields.Int(required=True)

    @validates("username")
    def validate_username(self, value):
        """Filter out responses with empty characters.

        :param value: value to validate
        """
        if value.strip() == "":
            raise ValidationError("username cannot be an empty string.")

    @validates("skin")
    def validate_skin(self, value: int):
        """Filter out responses with invalid skins.

        :param value: value to validate
        """
        if value > 10 or value < 1:
            raise ValidationError("skin does not exist.")


class ScoredSchema(Schema):
    points = fields.Int(required=True)

    @validates("points")
    def validate_points(self, value):
        """Filter out responses with invalid points"""
        if value >= 0 or value <= 6:
            raise ValidationError("points are not active")


class StartRequestSchema(Schema):
    username = fields.Str(required=True)
    skin = fields.Int(required=True)
    rounds = fields.Int(required=True)
    lap_time = fields.Int(required=True, data_key="lapTime")
    amount_users = fields.Int(required=True, data_key="amountUsers")

    @validates("username")
    def validate_username(self, value):
        """Filter out responses with empty characters.

        :param value: value to validate
        """
        if value.strip() == "":
            raise ValidationError("username cannot be an empty string.")

    @validates("skin")
    def validate_skin(self, value: int):
        """Filter out responses with invalid skins.

        :param value: value to validate
        """
        if value > 10 or value < 1:
            raise ValidationError("skin does not exist.")

    @validates("rounds")
    def validate_rounds(self, value):
        """Filter out responses invalid rounds.

        :param value: value to validate
        """
        if value < 1 or value > 5:
            raise ValidationError("invalid 'rounds' param.")

    @validates("lap_time")
    def validate_lap_time(self, value):
        """Filter out responses invalid lap_time.

        :param value: value to validate
        """
        if value < 1 or value > 60:
            raise ValidationError("invalid 'lap_time' param.")

    @validates("amount_users")
    def validate_amount_users(self, value):
        """Filter out responses invalid amount_users.

        :param value: value to validate
        """
        if value < 1 or value > 10:
            raise ValidationError("invalid 'amount_users' param.")
