from db import db
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import TagsSchema,TagAndItemSchema
from models import TagsModel,StoreModel,ItemModel
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required


blp=Blueprint("Tags",__name__,description="Operations on Tags")

@blp.route("/store/<int:store_id>/tags")
class Tags(MethodView):
    @jwt_required()
    @blp.response(200,TagsSchema(many=True))
    def get(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        return store.tags
    

    @jwt_required()
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
    

@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class LinkTagsToItem(MethodView):
    @jwt_required()
    @blp.response(200,TagsSchema)
    def post(self,item_id,tag_id):
        item=ItemModel.query.get_or_404(item_id)
        tag=TagsModel.query.get_or_404(tag_id)
        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(400,message="Error while occuring in LinkTagsToItem")

        return tag
    
    @jwt_required()
    @blp.response(200,TagAndItemSchema)
    def delete(self,item_id,tag_id):
        item=ItemModel.query.get_or_404(item_id)
        tag=TagsModel.query.get_or_404(tag_id)
        item.tags.remove(tag)
        
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(400,message="Error in delete item and tag link")

        return {"message":"Tag Deleted"}



@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @jwt_required()
    @blp.response(200,TagsSchema)
    def get(self,tag_id):
        tag=TagsModel.query.get_or_404(tag_id)
        return tag
    

    @jwt_required()
    @blp.response(200,
                description="Deletes a tag if no item is tagged with it.",
                example={"message": "Tag deleted."},
                  )
    def delete(self, tag_id):
        tag = TagsModel.query.get_or_404(tag_id)

        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted."}
        abort(
            400,
            message="Could not delete tag. Make sure tag is not associated with any items, then try again.",  # noqa: E501
        )

