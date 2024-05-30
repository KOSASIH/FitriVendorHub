from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class EventSchema(Schema):
    event_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    event_type = fields.Str(required=True)
    event_data = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
