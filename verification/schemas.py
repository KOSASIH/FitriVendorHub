from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class VerificationSchema(Schema):
    verification_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    code = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
