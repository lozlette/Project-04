from app import db, ma
from marshmallow import fields

ingredients_recipes = db.Table(
    'ingredients_recipes',
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
)

class Recipe(db.Model):

    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    extra_ingredients = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(1000), nullable=False)
    ingredients = db.relationship('Ingredient', secondary=ingredients_recipes, backref='recipes')

class RecipeSchema(ma.ModelSchema):

    ingredient = fields.Nested('IngredientSchema', many=True, exclude=('recipes'))

    class Meta:
        model = Recipe
