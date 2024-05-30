from marshmallow import Schema, fields

class DeviceSchema(Schema):
    device_id = fields.Int(dump_only=True)
    platform = fields.Str(required=True)
    model = fields.Str(required=True)
    os_version = fields.Str(required=True)

class MobileUserSchema(Schema):
    mobile_user_id = fields.Int(dump_only=True)
    device_id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class NotificationSchema(Schema):
    notification_id = fields.Int(dump_only=True)
    mobile_user_id = fields.Int(required=True)
    message = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
