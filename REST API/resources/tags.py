from db import db
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import TagsSchema
from models import TagsModel,StoreModel
from sqlalchemy.exc import SQLAlchemyError


blp=Blueprint("Tags",__name__,description="Operations on Tags")

@blp.route("/store/<string:store_id>/tags")
class Tags(MethodView):
    @blp.response(200,TagsSchema(many=True))
    def get(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        return store.tags.all()
    
    @blp.arguments(TagsSchema)
    @blp.response(200,TagsSchema)
    def post(self,tag_data,store_id):
        tags=TagsModel(**tag_data,store_id=store_id)
        try:
            db.session.add(tags)
            db.session.commit()
        except SQLAlchemyError:
            abort(400,message="Error While Inserting Tag details")

        return tags

@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200,TagsSchema)
    def get(self,tag_id):
        tag=TagsModel.query.get_or_404(tag_id)
        return tag

