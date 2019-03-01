from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema

ingredients_recipes = db.Table(
    'ingredients_recipes',
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
)

class Recipe(db.Model, BaseModel):

    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    extra_ingredients = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(1000), nullable=False)
    ingredients = db.relationship('Ingredient', secondary=ingredients_recipes, backref='recipes')


class RecipeSchema(ma.ModelSchema, BaseSchema):

    ingredients = fields.Nested('IngredientSchema', many=True, exclude=('recipes',))
    comments = fields.Nested('CommentSchema', many=True, exclude=('recipe',))

    class Meta:
        model = Recipe
