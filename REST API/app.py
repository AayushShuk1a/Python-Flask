from flask import Flask,request

app=Flask(__name__)


stores=[
    {
        "name":"MyStore",
        "items":[
            {
                "name":"Monitor",
                "price":20.99
            }
        ]
    }
]

@app.get("/store")
def getStore():
    return {"Stores":stores},200

@app.post("/store")
def createStore():
    request_data=request.get_json()
    newStore={"name":request_data["name"],"items":[]}
    stores.append(newStore)
    return newStore,201

@app.post("/store/<string:name>/item")
def createItems(name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={
                "name":request_data["name"],
                "price":request_data["price"]
            }
            store["items"].append(new_item)
            return new_item,201
    return "Store Not Found",404


@app.get("/store/<string:name>")
def getSingleStore(name):
    for store in stores:
        if store["name"]==name:
            return store,202
        
    return "Store Not Found",404

@app.get("/store/<string:name>/items")
def getAllItems(name):
    for store in stores:
        if store["name"]==name:
            return {"items":store["items"]},200
        
    return "Store Not Found",404