from marshmallow import Schema, fields, validate

class VendorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True, validate=validate.Length(min=5, max=100))
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=15))
    address = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    description = fields.Str(allow_none=True, validate=validate.Length(min=0, max=1000))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True, validate=validate.Length(min=0, max=1000))
    price = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    vendor_id = fields.Int(required=True)
    inventory = fields.Int(required=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    rating = fields.Int(required=True, validate=validate.Range(min=1, max=5))
    comment = fields.Str(allow_none=True, validate=validate.Length(min=0, max=1000))
    customer_id = fields.Int(required=True)
    vendor_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class RecommendationSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    score = fields.Float(required=True, validate=validate.Range(min=0, max=1))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class InventorySchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    vendor_id = fields.Int(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ShippingSchema(Schema):
    id = fields.Int(dump_only=True)
    vendor_id = fields.Int(required=True)
    shipping_provider = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    shipping_cost = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class LoyaltySchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    points = fields.Int(required=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class AnalyticsSchema(Schema):
    id = fields.Int(dump_only=True)
    vendor_id= fields.Int(required=True)
    sales = fields.Int(required=True, validate=validate.Range(min=0))
    customer_engagement = fields.Int(required=True, validate=validate.Range(min=0))
    product_performance = fields.Int(required=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class SocialSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    platform = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ChatbotSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    message = fields.Str(required=True, validate=validate.Length(min=1, max=1000))
    response = fields.Str(allow_none=True, validate=validate.Length(min=0, max=1000))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class VerificationSchema(Schema):
    id = fields.Int(dump_only=True)
    vendor_id = fields.Int(required=True)
    status = fields.Str(required=True, validate=validate.OneOf(["pending", "approved", "rejected"]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class MobileSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    device_type = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    device_token = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class GamificationSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    score = fields.Int(required=True, validate=validate.Range(min=0))
    rank = fields.Int(required=True, validate=validate.Range(min=1))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class MarketingSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    campaign_id = fields.Int(required=True)
    opened = fields.Bool(required=True)
    clicked = fields.Bool(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
