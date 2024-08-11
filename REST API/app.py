from flask import Flask
from flask_smorest import Api
from resources.items import blp as ItemBlueprint
from resources.store import blp as StoresBlueprint
from resources.tags import blp as TagsBlueprint
from db import db
import os
from flask_jwt_extended import JWTManager



def create_app(db_url=None):
    app=Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]=True
    app.config["API_TITLE"]="Stores REST API"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.init_app(app)

    app.config["JWT_SECRET_KEY"]="8169475793815650552307623615614161458"
    jwt=JWTManager(app)


    with app.app_context():
        db.create_all()

    api=Api(app)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoresBlueprint)
    api.register_blueprint(TagsBlueprint)
    return app      
