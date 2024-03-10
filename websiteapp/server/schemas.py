from marshmallow import Schema, fields

class EntityProductSchema(Schema):
    product_id = fields.Str(required=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)
    supplier = fields.Str(required=True)

class EntityUserSchema(Schema):
    customer_id = fields.Str(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)
    created_date = fields.Str(required=True)
    last_login = fields.Str(required=True)