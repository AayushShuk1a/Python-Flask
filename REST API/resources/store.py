import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import stores

blp=Blueprint("stores",__name__,description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
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

    def put(self,store_id):
        request_data=request.get_json()
        if "name" not in request_data:
            abort(404,message="Include Name in JSON payload")
        try:
            store=stores[store_id]
            store |= request_data
            return store
        except KeyError:
            abort(404,message="Store Not Found")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores":list(stores.values())}
    
    def post(self):
        request_data=request.get_json()
        if "name" not in request_data:
            abort(404,message="Name is not present in JSON")
        for store in stores.values():
            if request_data["name"]==store["name"]:
                abort(404,"Store Aleady Exist")
        store_id=uuid.uuid4().hex
        newStore={**request_data,"id":store_id}
        stores[store_id]=newStore
        return newStore,201
        
