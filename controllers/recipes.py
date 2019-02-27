from flask import Blueprint
from models.recipe import Recipe, RecipeSchema
from lib.secure_route import secure_route

api = Blueprint('recipes', __name__)

recipes_schema = RecipeSchema(many=True)
recipe_schema = RecipeSchema()

@api.route('/recipes', methods=['GET'])
@secure_route
def index():
    recipes = Recipe.query.all()
    return recipes_schema.jsonify(recipes)

@api.route('/recipes/<int:recipe_id>', methods=['GET'])
@secure_route
def show(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return recipe_schema.jsonify(recipe)
