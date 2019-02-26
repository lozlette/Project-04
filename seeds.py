from app import app, db
from models.ingredient import Ingredient

with app.app_context():
    db.drop_all()
    db.create_all()

banana = Ingredient(
name='Banana',
image_url='https://i5.walmartimages.ca/images/Enlarge/580/6_r/875806_R.jpg',
nutrition_information='Vitamin B6 - 0.5 mg, Manganese - 0.3 mg, Vitamin C - 9 mg, Potassium - 450 mg, Dietary Fiber - 3g, Protein - 1 g, Magnesium - 34 mg, Folate - 25.0 mcg.')
db.session.add(banana)



db.session.commit()
