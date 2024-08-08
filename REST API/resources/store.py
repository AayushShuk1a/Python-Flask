from db import db
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import StoreSchema,updateStoreSchema
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from models import StoreModel

blp=Blueprint("stores",__name__,description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404,message="Store not found")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message":"Item Deleted"}
        except KeyError:
            abort(404,message="Store Not Found")

    @blp.arguments(updateStoreSchema)
    @blp.response(200,StoreSchema)
    def put(self,request_data,store_id):
        try:
            store=stores[store_id]
            store |= request_data
            return store
        except KeyError:
            abort(404,message="Store Not Found")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return stores.values()
    
    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self,request_data):
        store=StoreModel(**request_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400,message="Name Already Exist")
        except SQLAlchemyError:
            abort(400,message="Error Occured while adding store")
        
        return store,201
        
