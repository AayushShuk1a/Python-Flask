from flask import Flask,jsonify
from flask_smorest import Api
from resources.items import blp as ItemBlueprint
from resources.store import blp as StoresBlueprint
from resources.tags import blp as TagsBlueprint
from resources.users import blp as UserBlueprint
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

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header,jwt_payload):
        return (
            jsonify(
                {"message":"The Token Has Expired.","error":"Token Expired"}
            ),401
        )
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message":"Signature Verification Failed.","error":"Invalid Token"}
            ),401
        )
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {"message":"Request does not contain an access Token.","error":"authorization_required"}
            ),401
        )

    with app.app_context():
        db.create_all()

    api=Api(app)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoresBlueprint)
    api.register_blueprint(TagsBlueprint)
    api.register_blueprint(UserBlueprint)
    return app      
