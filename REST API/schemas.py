from marshmallow import Schema,fields

class PlainitemSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    price=fields.Float(required=True)

class PlainStoreSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)

class PlainTagsSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)


class itemUpdateSchema(Schema):
    name=fields.Str()
    price=fields.Float()

class updateStoreSchema(Schema):
    name=fields.Str(required=True)

class updateTagSchema(Schema):
    name=fields.Str(required=True)


class itemSchema(PlainitemSchema):
    store_id=fields.Int(required=True,load_only=True)
    stores=fields.Nested(PlainStoreSchema,dump_only=True)


class StoreSchema(PlainStoreSchema):
    items=fields.Nested(PlainitemSchema,many=True,dump_only=True)
    tags=fields.Nested(PlainTagsSchema,many=True,dump_only=True)

class TagsSchema(PlainTagsSchema):
    store_id=fields.Int(load_only=True)
    stores=fields.Nested(PlainStoreSchema,dump_only=True)