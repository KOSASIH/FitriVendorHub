from marshmallow import Schema, fields

class RecommendationSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    score = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class RecommendationFeatureSchema(Schema):
    id = fields.Int(dump_only=True)
    recommendation_id = fields.Int(required=True)
    feature_name = fields.Str(required=True)
    feature_value = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
