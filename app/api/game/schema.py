""" schema.py """
from marshmallow import Schema, fields


class GameStatusResponseSchema(Schema):
    started_at = fields.Int(dumps_only=True, data_key="startedAt")
    rounds = fields.Int(dumps_only=True)
    lap_time = fields.Int(dumps_only=True, data_key="lapTime")
    users = fields.List(fields.Dict(keys=fields.Str(), values=fields.Str()))
    words = fields.List(fields.List(fields.Str()))

