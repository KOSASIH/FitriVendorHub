from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
