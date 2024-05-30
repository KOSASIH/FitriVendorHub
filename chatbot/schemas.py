from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class ConversationSchema(Schema):
    conversation_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    created_at = fields.DateTime(required=True)

class MessageSchema(Schema):
    message_id = fields.Int(dump_only=True)
    conversation_id = fields.Int(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
