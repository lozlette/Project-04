from app import db, ma
from .base import BaseModel, BaseSchema

class Comment(db.Model, BaseModel):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User', backref='comments')
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipes = db.relationship('Recipe', backref='comments')


class CommentSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Comment
