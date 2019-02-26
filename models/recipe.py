from app import db, ma

class Recipe(db.Model):

    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    extra_ingredients = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(1000), nullable=False)

class RecipeSchema(ma.ModelSchema):

    class Meta:
        model = Recipe
