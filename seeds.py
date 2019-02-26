from app import app, db
from models.ingredient import Ingredient
from models.recipe import Recipe

with app.app_context():
    db.drop_all()
    db.create_all()

banana = Ingredient(
name='Banana',
image_url='https://i5.walmartimages.ca/images/Enlarge/580/6_r/875806_R.jpg',
nutrition_information='Vitamin B6 - 0.5 mg, Manganese - 0.3 mg, Vitamin C - 9 mg, Potassium - 450 mg, Dietary Fiber - 3g, Protein - 1 g, Magnesium - 34 mg, Folate - 25.0 mcg.')
db.session.add(banana)

banana_bread = Recipe(
name='Banana Bread',
image_url='https://www.inspiredtaste.net/wp-content/uploads/2016/12/Easy-Banana-Bread-Recipe-1-1200.jpg',
extra_ingredients='140g butter, softened, plus extra for the tin, 140g caster sugar, 2 large eggs, beaten, 140g self-raising flour, 1 tsp baking powder, 2 very ripe bananas, mashed, 50g icing sugar, handful dried banana chips, for decoration',
method='1. Heat oven to 180C/160C fan/gas. 2. Butter a 2lb loaf tin and line the base and sides with baking parchment. 3. Cream 140g softened butter and 140g caster sugar until light and fluffy, then slowly add 2 beaten large eggs with a little of the 140g flour. 4. Fold in the remaining flour, 1 tsp baking powder and 2 mashed bananas. 5. Pour into the tin and bake for about 30 mins until a skewer comes out clean. 6. Cool in the tin for 10 mins, then remove to a wire rack. 7. Mix 50g icing sugar with 2-3 tsp water to make a runny icing. 8. Drizzle the icing across the top of the cake and decorate with a handful of banana chips.'
)
db.session.add(banana_bread)

db.session.commit()
