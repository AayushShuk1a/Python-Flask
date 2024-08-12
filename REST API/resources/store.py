from db import db
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import StoreSchema,updateStoreSchema
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from models import StoreModel

blp=Blueprint("stores",__name__,description="Operations on stores")


@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        return store

    def delete(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message":"Store Deleted!!"}

    @blp.arguments(updateStoreSchema)
    @blp.response(200,StoreSchema)
    def put(self,request_data,store_id):
        store=StoreModel.query.get(store_id)
        if store:
            store.name=request_data["name"]
        else:
            store=StoreModel(id=store_id,**request_data)

        db.session.add(store)
        db.session.commit()
        return store


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    
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
        
