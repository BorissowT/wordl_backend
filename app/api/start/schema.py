""" schema.py """

"""apartment_configs/schema.py

This package contains schema class for serialization and deserialization of
incoming and outgoing responses.

"""
from marshmallow import Schema, fields, validates, ValidationError, post_load


class StartResponseSchema(Schema):

    game_id = fields.Str(dumps_only=True)
    token = fields.Str(dumps_only=True)


class StartRequestSchema(Schema):

    username = fields.Str(required=True)
    skin = fields.Int(required=True)
    rounds = fields.Int(required=True)
    lap_time = fields.Int(required=True, data_key="lapTime")
    amount_users = fields.Int(required=True, data_key="amountUsers")

    @validates("username")
    def validate_apartment_id(self, value):
        """Filter out responses with empty characters.

        :param value: value to validate
        """
        if value.strip() == "":
            raise ValidationError("username cannot be an empty string.")

    @validates("skin")
    def validate_title(self, value: int):
        """Filter out responses with invalid skins.

        :param value: value to validate
        """
        if value > 10 or value < 1:
            raise ValidationError("skin does not exist.")

    @validates("rounds")
    def validate_configs(self, value):
        """Filter out responses invalid rounds.

        :param value: value to validate
        """
        if value < 1 or value > 5:
            raise ValidationError("invalid 'rounds' param.")

    @validates("lap_time")
    def validate_configs(self, value):
        """Filter out responses invalid lap_time.

        :param value: value to validate
        """
        if value < 1 or value > 60:
            raise ValidationError("invalid 'lap_time' param.")

    @validates("amount_users")
    def validate_configs(self, value):
        """Filter out responses invalid amount_users.

        :param value: value to validate
        """
        if value < 1 or value > 10:
            raise ValidationError("invalid 'amount_users' param.")

    @post_load
    def make_apartment_configs(self, data: dict, **kwargs):
        """Deserialize passed data to data model.

        :param data: data from response
        :param kwargs: other params
        :return: model instance
        """
        pass
