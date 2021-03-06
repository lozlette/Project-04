from flask import Blueprint, request, jsonify, g
from models.ingredient import Ingredient, IngredientSchema


api = Blueprint('ingredients', __name__)

ingredients_schema = IngredientSchema(many=True)
ingredient_schema = IngredientSchema()

@api.route('/ingredients', methods=['GET'])
def index():
    ingredients = Ingredient.query.all()
    return ingredients_schema.jsonify(ingredients)

@api.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def show(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)
    return ingredient_schema.jsonify(ingredient)
