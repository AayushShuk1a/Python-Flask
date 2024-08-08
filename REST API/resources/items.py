from db import db
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import itemSchema,itemUpdateSchema
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError

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
        item=ItemModel(**request_data)
        print(item)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            return abort(400,message="Error while inserting the item data")
        
        return item

