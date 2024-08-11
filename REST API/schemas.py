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
    stores=fields.Nested(PlainStoreSchema(),dump_only=True)
    tags=fields.List(fields.Nested(PlainTagsSchema(),dump_only=True))
    

class StoreSchema(PlainStoreSchema):
    items=fields.List(fields.Nested(PlainitemSchema(),dump_only=True))
    tags=fields.List(fields.Nested(PlainTagsSchema(),dump_only=True))

class TagsSchema(PlainTagsSchema):
    store_id=fields.Int(load_only=True)
    stores=fields.Nested(PlainStoreSchema(),dump_only=True)
    items=fields.List(fields.Nested(PlainitemSchema(),dump_only=True))

class TagAndItemSchema(Schema):
    message=fields.Str()
    item=fields.Nested(itemSchema)
    tags=fields.Nested(TagsSchema)


class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True,load_only=True)