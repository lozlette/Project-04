from app import db, ma
from .base import BaseModel, BaseSchema
from marshmallow import fields

class Comment(db.Model, BaseModel):

    __tablename__ = 'comments'

    content = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='comments')
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipe = db.relationship('Recipe', backref='comments')


class CommentSchema(ma.ModelSchema, BaseSchema):

    recipe = fields.Nested('RecipeSchema', exclude=('comments', ))
    user = fields.Nested('UserSchema', exclude=('comments', ))

    class Meta:
        model = Comment
