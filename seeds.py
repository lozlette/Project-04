from app import app, db
from models.ingredient import Ingredient
from models.recipe import Recipe
from models.user import User
from models.comment import Comment

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
method='1. Heat oven to 180C/160C fan/gas. 2. Butter a 2lb loaf tin and line the base and sides with baking parchment. 3. Cream 140g softened butter and 140g caster sugar until light and fluffy, then slowly add 2 beaten large eggs with a little of the 140g flour. 4. Fold in the remaining flour, 1 tsp baking powder and 2 mashed bananas. 5. Pour into the tin and bake for about 30 mins until a skewer comes out clean. 6. Cool in the tin for 10 mins, then remove to a wire rack. 7. Mix 50g icing sugar with 2-3 tsp water to make a runny icing. 8. Drizzle the icing across the top of the cake and decorate with a handful of banana chips.',
ingredients=[banana]
)
db.session.add(banana_bread)


carrot = Ingredient(
name='Carrot',
image_url='http://cdn.shopify.com/s/files/1/1380/2059/products/Carrot-Orange_grande.jpg?v=1480318421',
nutrition_information='Fiber: 2.8 g, Fat: 0.2 g, Calories: 41, Trans fat: ~')
db.session.add(carrot)

carrot_cheese_muffins = Recipe(
name='Carrot & Cheese Muffins',
image_url='https://www.annabelkarmel.com/wp-content/uploads/2019/02/Carrot-Cheese-and-herb-Muffins-1800x1800.jpg',
extra_ingredients='2 eggs, 175g self raising flour, 1 tsp baking powder, 100 ml milk,100g carrot, peeled and grated, 3 tbsp sunflower oil,1 tbsp chives, chopped,6 spring onions, sliced,1 tbsp fresh basil , chopped,50g parmesan, grated',
method='1.Preheat the oven to 180C Fan. Line a muffin tin with 10 muffin cases.2.Whisk the egg, flour, baking powder, milk and oil together in a large bowl. Add the carrot, herbs, spring onion and cheese and fold together. Spoon into the cases.3.Bake in the oven for 18 minutes until sell risen and lightly golden brown.',
ingredients=[carrot]
)
db.session.add(carrot_cheese_muffins)



spinach = Ingredient(
name='Spinach',
image_url='https://ats.org/wp-content/uploads/2016/09/spinach-leaves-1461774375kTU-700x466.jpg',
nutrition_information='Protein 2.9 g, Carbs 3.6 g, Sugar 0.4 g, Fiber 2.2 g, Fat 0.4 g, Saturated 0.06 g, Monounsaturated 0.01 g, Polyunsaturated 0.17 g, Omega-3 0.14 g ,Omega-6 0.03 g, Trans fat ~')

db.session.add(spinach)

salmon_broccoli_spinach_puree = Recipe(
name='Salmon, Broccoli & Spinach Puree',
image_url='https://www.annabelkarmel.com/wp-content/uploads/2016/10/Salmon_Broccoli_Puree-lowres-2-380x315.jpg',
extra_ingredients='A knob of butter,100g shallots, sliced,225g peeled potatoes, diced,300 ml water,225g salmon fillet, diced, 100g broccoli florets, 30g baby spinach, 75ml milk, 15g parmesan cheese, grated, A squeeze of lemon juice',
method='1.Melt the butter in a saucepan. Add the shallots and potatoes and fry for 2 minutes. Add the water, cover with a lid and simmer for 10 minutes. 2.Add the salmon and broccoli and cover and simmer for another 10 minutes until the vegetables are cooked through. Add the spinach two minutes before the end of the cooking time. 3.Add the milk and parmesan cheese. 4.Blend until smooth using an electric hand blender and the lemon juice.',
ingredients=[spinach]
)
db.session.add(salmon_broccoli_spinach_puree)


kale = Ingredient(
name='Kale',
image_url='https://cdn1.medicalnewstoday.com/content/images/articles/270/270435/dinosaur-kale.jpg',
nutrition_information=' 3 grams of protein, 2.5 grams of fiber, Vitamins A, C, and K, Folate, B vitamin, Alpha-linolenic acid, omega-3 fatty acid.')

db.session.add(kale)

sweet_potato_kale_croquettes = Recipe(
name='Sweet Potato and Kale Croquettes',
image_url='https://www.annabelkarmel.com/wp-content/uploads/2018/08/Sweet-potato-and-kale-croquettes_small2-380x315.jpg',
extra_ingredients='2 tbsp sunﬂ ower oil, 1 small onion, chopped, 100g (31/2oz) mushrooms, chopped, 1 medium carrot, grated, 20g (3/4oz) kale, chopped, 1 garlic clove, crushed, 150g (5 1/2oz) baking potato, pricked, 150g (5 1/2oz) sweet potato, pricked, 50g (1 3/4oz) fresh breadcrumbs or wheat- or gluten-free breadcrumbs, 30g (1oz) Cheddar cheese or dairy-free alternative, grated, Plain ﬂour or gluten-free ﬂour, to coat',
method='Heat 1 tablespoon of the oil in a frying pan. Add the onion, mushrooms, carrot, kale, and garlic, and fry for 5 minutes over a medium heat. Leave to cool. 2.Cook the potatoes in a microwave for 10 minutes until soft. Leave to cool, then scoop out the potato ﬂ esh into a bowl. 3. Add the cooked vegetables, breadcrumbs, and cheese and mix together until blended. Shape into 14 small croquettes and roll in the ﬂour. 4.Heat the remaining 1 tablespoon of oil in a frying pan. Fry the croquettes for 3–4 minutes, until golden on all sides and cooked through. Drain on kitchen paper and leave to cool before serving. 5.When needed, thaw overnight in the fridge or leave out for a few hours at room temperature. Reheat in an oven preheated to 180ºC (fan 160ºC), gas 4 for 10–12 minutes.',
ingredients=[kale]
)
db.session.add(sweet_potato_kale_croquettes)


apple = Ingredient(
name='Apple',
image_url='https://5.imimg.com/data5/YY/EN/MY-8155364/fresh-apple-500x500.jpg',
nutrition_information=' Protein 0.3 g,Carbs 13.8 g, Sugar 10.4 g, Fiber 2.4 g, Fat 0.2 g, Saturated 0.03 g, Monounsaturated 0.01 g, Polyunsaturated 0.05 g, Omega-3 0.01 g, Omega-6 0.04 g, Trans fat 0 g')

db.session.add(apple)

butternut_squash_apple_prune = Recipe(
name='Butternut Squash, Apple and Prune',
image_url='https://www.annabelkarmel.com/wp-content/uploads/2017/07/Butternut-Squash-Carrot-and-Apple-380x315.png',
extra_ingredients='100 g 1 medium carrot, peeled and sliced, 200 g butternut squash, peeled, deseeded and chopped,50 g 1 small dessert apple, peeled, cored and chopped, 10 g prunes, chopped',
method='1.Put the carrot and squash into a steamer and cook for 5 minutes. 2.Add the apple and prunes and continue to steam for 10 minutes, until all the ingredients are tender. 3.Blend with about 2 tablespoons of water from the steamer. s4.Serve with breast milk or formula if serving as First Foods Lunch.',
ingredients=[apple]
)
db.session.add(butternut_squash_apple_prune)


pepper = Ingredient(
name='Pepper',
image_url='https://target.scene7.com/is/image/Target/GUEST_7c2f5da1-86b0-41c7-83a5-a21359f82e6e?wid=488&hei=488&fmt=pjpeg',
nutrition_information=' Potassium 340 mg, Carbohydrate 9 g, Dietary fiber 1.5 g, Sugar 5 g, Protein 2 g, Vitamin A 23%, Vitamin C 404%, Calcium 1%, Iron 6%, Vitamin D 0%, Vitamin B-6 15%, Cobalamin 0%, Magnesium 6%')

db.session.add(pepper)

spiralized_vegetables_roasted_red_pepper_tomato_pesto = Recipe(
name='Spiralized Vegetables with Roasted Red Pepper & Tomato Pesto',
image_url='https://www.annabelkarmel.com/wp-content/uploads/2015/08/Spiralized_Vegetables_with_Roasted_Red_Pepper_and_Tomato_Pesto-3-380x315.jpg',
extra_ingredients='2 Romero red peppers, deseeded & roughly chopped,650 g cherry tomatoes, halved, 8 tbsp olive oil,3 cloves garlic,100 g pine nuts, toasted, 75 g Italian hard-style cheese, grated,30 g basil, chopped, 1/4 red chilli, deseeded & diced, 5 large courgettes, 4 large carrots, peeled',
method='1.Preheat the oven to 140 Fan. To make the pesto, put the peppers onto a baking sheet. Drizzle over 1 tbsp of oil and season. 2.Put the tomatoes onto a baking sheet. Drizzle over 1 tbsp of oil and season. 3.Put both baking sheets into the oven for 45 minutes until semi dried. Leave to cool. 4.Put the cold peppers and tomatoes into a food processor with the remaining oil, garlic, 75g of pinenuts, basil, cheese and chilli. Whiz until smooth and season. 5.Put the courgettes and carrots through a spiralizer to make long spaghetti. Heat a frying pan until hot. Add a little oil. Quickly fry the carrots for 4 – 5 minutes then add the courgettes for 2 minutes, tossing together lightly. 6.Warm the pesto and mix with the vegetables and reserved pinenuts.',
ingredients=[pepper]
)
db.session.add(spiralized_vegetables_roasted_red_pepper_tomato_pesto)

lauren = User(
name='Lauren',
email='lauren@bell.com',
password_hash='password',
avatar='https://workhound.com/wp-content/uploads/2017/05/placeholder-profile-pic.png'
)
db.session.add(lauren)

gessica = User(
name='Gessica',
email='gessica@mail.com',
password_hash='password1',
avatar='https://www.whatsappprofiledpimages.com/wp-content/uploads/2018/07/awesome-profile-pics-300x300.jpg'
)
db.session.add(gessica)
comment1 = Comment(content='This is a yummy recipe.', recipes=banana_bread, users=lauren)
db.session.add(comment1)

db.session.commit()
