from db import db
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import itemSchema,itemUpdateSchema
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

blp=Blueprint("Items",__name__,description="Operations on Items")


@blp.route("/items/<int:item_id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200,itemSchema)
    def get(self,item_id):
        item=ItemModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self,item_id):
        item=ItemModel.query.get(item_id)
        db.session.delete(item)
        db.session.commit()
        return "Item Deleted!!"

    @jwt_required()
    @blp.arguments(itemUpdateSchema)
    @blp.response(200,itemSchema)
    def put(self,request_data,item_id):
        item=ItemModel.query.get(item_id)
        if item:
            item.name=request_data["name"]
            item.price=request_data["price"]
        else:
            item=ItemModel(id=item_id,**request_data)
        
        db.session.add(item)
        db.session.commit()
        return item

@blp.route("/items")
class Items(MethodView):
    @jwt_required()
    @blp.response(200,itemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @jwt_required()
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

