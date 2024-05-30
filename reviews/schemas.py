from marshmallow import Schema, fields

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    rating = fields.Int(required=True)
    comment = fields.Str(allow_none=True)
    customer_id = fields.Int(required=True)
    vendor_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ReviewImageSchema(Schema):
    id = fields.Int(dump_only=True)
    review_id = fields.Int(required=True)
    image_url = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
