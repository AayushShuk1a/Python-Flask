from flask import Flask

app=Flask(__name__)


stores=[
    {
        "name":"MyStore",
        "Items":[
            {
                "name":"Monitor",
                "price":20.99
            }
        ]
    }
]

@app.get("/store")
def getStore():
    return {"Stores":stores}