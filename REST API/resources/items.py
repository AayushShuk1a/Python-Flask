import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items,stores

blp=Blueprint("Items",__name__,description="Operations on Items")


@blp.route("/items/<string:item_id>")
class Item(MethodView):
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

    def put(self,item_id):
        request_data=request.get_json()
        if(
            "name" not in request_data
            or "price" not in request_data
        ):
            abort(404,message="Ensure to add name and price in JSON payload")

        try:
            item=items[item_id]
            item|=request_data
            return item
        except KeyError:
            abort(404,message="Item Not Found")


@blp.route("/items")
class Items(MethodView):
    def get(self):
        return {"items":list(items.values())}
    
    def post(self):
        request_data=request.get_json()
        if("name" not in request_data
        or "price" not in request_data
        or "store_id" not in request_data
        ):
            abort(404,message="Ensure name, pirce, store_id is mentioned in JSON data")
        
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

