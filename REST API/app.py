from flask import Flask,request
import uuid
from db import stores,items

app=Flask(__name__)

@app.get("/store")
def getStore():
    return {"stores":list(stores.values())}


@app.post("/store")
def createStore():
    request_data=request.get_json()
    store_id=uuid.uuid4().hex
    newStore={**request_data,"id":store_id}
    stores[store_id]=newStore
    return newStore,201

@app.post("/store/item")
def createItems():
    request_data=request.get_json()
    if request_data["store_id"] not in stores:
        return "Store Not Found"
    item_id=uuid.uuid4().hex
    new_item={**request_data,"id":item_id}
    items[item_id]=new_item
    return new_item,201


@app.get("/store/<string:store_id>")
def getSingleStore(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return "Store Not Found",404
    
@app.get("/store/<string:item_id>")
def getItem(item_id):
    try:
        return items[item_id]
    except KeyError:
        return "Item Not Found",404

@app.get("/store/items")
def getAllItems(): 
    return {"items":list(items.values())}