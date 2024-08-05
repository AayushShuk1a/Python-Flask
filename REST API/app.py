from flask import Flask,request
import uuid
from db import stores,items
from flask_smorest import abort

app=Flask(__name__)

@app.get("/store")
def getStore():
    return {"stores":list(stores.values())}

@app.get("/store/<string:store_id>")
def getSingleStore(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message="Store not found")

@app.post("/store")
def createStore():
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

@app.delete("/store/<string:store_id>")
def deleteStore(store_id):
    try:
        del stores[store_id]
        return {"message":"Item Deleted"}
    except KeyError:
        abort(404,message="Store Not Found")

@app.put("/store/<string:store_id>")
def updateStore(store_id):
    request_data=request.get_json()
    if "name" not in request_data:
        abort(404,message="Include Name in JSON payload")
    try:
        store=stores[store_id]
        store |= request_data
        return store
    except KeyError:
        abort(404,message="Store Not Found")

@app.get("/store/<string:item_id>")
def getItem(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message="Item not found")

@app.get("/store/items")
def getAllItems(): 
    return {"items":list(items.values())}

@app.post("/store/item")
def createItems():
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


@app.delete("/item/<string:item_id>")
def deleteItem(item_id):
    try:
        del items[item_id]
        return {"message":"Item Deleted"}
    except KeyError:
        abort(404,message="Item not found")

@app.put("/item/<string:item_id>")
def updateItems(item_id):
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
    

    
