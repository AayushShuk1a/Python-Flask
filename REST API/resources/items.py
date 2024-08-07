import uuid
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items,stores
from schemas import itemSchema,itemUpdateSchema

blp=Blueprint("Items",__name__,description="Operations on Items")


@blp.route("/items/<string:item_id>")
class Item(MethodView):
    @blp.response(200,itemSchema)
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404,message="Item not found")

    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message":"Item Deleted"}
        except KeyError:
            abort(404,message="Item not found")

    @blp.arguments(itemUpdateSchema)
    @blp.response(200,itemSchema)
    def put(self,request_data,item_id):
        try:
            item=items[item_id]
            item|=request_data
            return item
        except KeyError:
            abort(404,message="Item Not Found")


@blp.route("/items")
class Items(MethodView):
    @blp.response(200,itemSchema(many=True))
    def get(self):
        return items.values()
    
    @blp.arguments(itemSchema)
    @blp.response(200,itemSchema)
    def post(self,request_data):
        for item in items.values():
            if(item["name"]==request_data["name"]
            and item["store_id"]==request_data["store_id"]
            ):
                abort(404,message="Item Already Exist")
        
        if request_data["store_id"] not in stores:
            abort(404,message="Store Not Found")
        item_id=uuid.uuid4().hex
        new_item={**request_data,"id":item_id}
        items[item_id]=new_item
        return new_item,201

