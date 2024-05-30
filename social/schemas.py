from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)

class PostSchema(Schema):
    post_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(required=True)

class CommentSchema(Schema):
    comment_id = fields.Int(dump_only=True)
    post_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
