from marshmallow import Schema, fields

class CustomerSchema(Schema):
    customer_id = fields.Int(dump_only=True)
    phone_number = fields.Str(required=True)
    country_code = fields.Str(required=True)
    loyalty_points = fields.Int()

class SalesTransactionSchema(Schema):
    transaction_id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    transaction_price = fields.Int(required=True)
    transaction_date = fields.DateTime(required=True)
