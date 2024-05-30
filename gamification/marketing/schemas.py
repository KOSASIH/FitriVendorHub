from marshmallow import Schema, fields

class CampaignSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    budget = fields.Float(required=True)
    actual_spend = fields.Float(required=True)
    conversion_rate = fields.Float(required=True)
    status = fields.Str(required=True)

class ChannelSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    campaigns = fields.Nested('CampaignSchema', many=True)

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    campaigns = fields.Nested('CampaignSchema', many=True)
