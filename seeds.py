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
image='https://i5.walmartimages.ca/images/Enlarge/580/6_r/875806_R.jpg',
nutrition_information='Vitamin B6 - 0.5 mg, Manganese - 0.3 mg, Vitamin C - 9 mg, Potassium - 450 mg, Dietary Fiber - 3g, Protein - 1 g, Magnesium - 34 mg, Folate - 25.0 mcg.')
db.session.add(banana)

banana_carrot_seed_bread = Recipe(
name='BLW Banana, Carrot and Seed Bread',
image='https://www.annabelkarmel.com/wp-content/uploads/2017/05/412243735Loaf_Work-e1493997814752-380x315.jpg',
extra_ingredients='150g / 5oz softened unsalted butter, 2 large eggs, 200g/ 7oz ripe bananas, peeled and mashed, 125g / 4½oz grated carrot, 25g / 1oz sultanas, 125g / 4½oz soft dark brown sugar, 225g / 8oz self-raising flour, ½ teaspoon ground cinnamon, 1 teaspoon mixed spice, 1 teaspoon ground ginger, 25g / 1oz pumpkin seeds, 25g / 1oz sunflower seeds, Butter, for spreading and greasing',
method='1.Preheat the oven to 170°C/340°F/Gas 3, grease a 900 g/2 lb loaf tin and line it with baking parchment.2.Place all of the ingredients, except the topping, in a large mixing bowl. Whisk together with an electric hand-held whisk for 1–2 minutes until light and fluffy. Alternatively, use a stand mixer fitted with the paddle or whisk attachment. 3.Spoon the mixture into the tin and level out the top. 4.Sprinkle with the extra seeds and bake for 1–1¼ hours until golden, well risen and a skewer inserted comes out clean. 5.Remove from the oven and leave to cool on a wire rack, then remove from the tin. Dust with icing sugar (if using), cut into slices, spread with butter and serve.',
ingredients=[banana]
)
db.session.add(banana_carrot_seed_bread)


carrot = Ingredient(
name='Carrot',
image='http://cdn.shopify.com/s/files/1/1380/2059/products/Carrot-Orange_grande.jpg?v=1480318421',
nutrition_information='Fiber: 2.8 g, Fat: 0.2 g, Calories: 41, Trans fat: ~')
db.session.add(carrot)

carrot_cheese_muffins = Recipe(
name='Carrot & Cheese Muffins',
image='https://www.annabelkarmel.com/wp-content/uploads/2019/02/Carrot-Cheese-and-herb-Muffins-1800x1800.jpg',
extra_ingredients='2 eggs, 175g self raising flour, 1 tsp baking powder, 100 ml milk,100g carrot, peeled and grated, 3 tbsp sunflower oil,1 tbsp chives, chopped,6 spring onions, sliced,1 tbsp fresh basil , chopped,50g parmesan, grated',
method='1.Preheat the oven to 180C Fan. Line a muffin tin with 10 muffin cases.2.Whisk the egg, flour, baking powder, milk and oil together in a large bowl. Add the carrot, herbs, spring onion and cheese and fold together. Spoon into the cases.3.Bake in the oven for 18 minutes until sell risen and lightly golden brown.',
ingredients=[carrot]
)
db.session.add(carrot_cheese_muffins)



spinach = Ingredient(
name='Spinach',
image='https://ats.org/wp-content/uploads/2016/09/spinach-leaves-1461774375kTU-700x466.jpg',
nutrition_information='Protein 2.9 g, Carbs 3.6 g, Sugar 0.4 g, Fiber 2.2 g, Fat 0.4 g, Saturated 0.06 g, Monounsaturated 0.01 g, Polyunsaturated 0.17 g, Omega-3 0.14 g ,Omega-6 0.03 g, Trans fat ~')

db.session.add(spinach)

salmon_broccoli_spinach_puree = Recipe(
name='Salmon, Broccoli & Spinach Puree',
image='https://www.annabelkarmel.com/wp-content/uploads/2016/10/Salmon_Broccoli_Puree-lowres-2-380x315.jpg',
extra_ingredients='A knob of butter,100g shallots, sliced,225g peeled potatoes, diced,300 ml water,225g salmon fillet, diced, 100g broccoli florets, 30g baby spinach, 75ml milk, 15g parmesan cheese, grated, A squeeze of lemon juice',
method='1.Melt the butter in a saucepan. Add the shallots and potatoes and fry for 2 minutes. Add the water, cover with a lid and simmer for 10 minutes. 2.Add the salmon and broccoli and cover and simmer for another 10 minutes until the vegetables are cooked through. Add the spinach two minutes before the end of the cooking time. 3.Add the milk and parmesan cheese. 4.Blend until smooth using an electric hand blender and the lemon juice.',
ingredients=[spinach]
)
db.session.add(salmon_broccoli_spinach_puree)


kale = Ingredient(
name='Kale',
image='https://cdn1.medicalnewstoday.com/content/images/articles/270/270435/dinosaur-kale.jpg',
nutrition_information=' 3 grams of protein, 2.5 grams of fiber, Vitamins A, C, and K, Folate, B vitamin, Alpha-linolenic acid, omega-3 fatty acid.')

db.session.add(kale)

sweet_potato_kale_croquettes = Recipe(
name='Sweet Potato and Kale Croquettes',
image='https://www.annabelkarmel.com/wp-content/uploads/2018/08/Sweet-potato-and-kale-croquettes_small2-380x315.jpg',
extra_ingredients='2 tbsp sunﬂ ower oil, 1 small onion, chopped, 100g (31/2oz) mushrooms, chopped, 1 medium carrot, grated, 20g (3/4oz) kale, chopped, 1 garlic clove, crushed, 150g (5 1/2oz) baking potato, pricked, 150g (5 1/2oz) sweet potato, pricked, 50g (1 3/4oz) fresh breadcrumbs or wheat- or gluten-free breadcrumbs, 30g (1oz) Cheddar cheese or dairy-free alternative, grated, Plain ﬂour or gluten-free ﬂour, to coat',
method='Heat 1 tablespoon of the oil in a frying pan. Add the onion, mushrooms, carrot, kale, and garlic, and fry for 5 minutes over a medium heat. Leave to cool. 2.Cook the potatoes in a microwave for 10 minutes until soft. Leave to cool, then scoop out the potato ﬂ esh into a bowl. 3. Add the cooked vegetables, breadcrumbs, and cheese and mix together until blended. Shape into 14 small croquettes and roll in the ﬂour. 4.Heat the remaining 1 tablespoon of oil in a frying pan. Fry the croquettes for 3–4 minutes, until golden on all sides and cooked through. Drain on kitchen paper and leave to cool before serving. 5.When needed, thaw overnight in the fridge or leave out for a few hours at room temperature. Reheat in an oven preheated to 180ºC (fan 160ºC), gas 4 for 10–12 minutes.',
ingredients=[kale]
)
db.session.add(sweet_potato_kale_croquettes)


apple = Ingredient(
name='Apple',
image='https://5.imimg.com/data5/YY/EN/MY-8155364/fresh-apple-500x500.jpg',
nutrition_information=' Protein 0.3 g,Carbs 13.8 g, Sugar 10.4 g, Fiber 2.4 g, Fat 0.2 g, Saturated 0.03 g, Monounsaturated 0.01 g, Polyunsaturated 0.05 g, Omega-3 0.01 g, Omega-6 0.04 g, Trans fat 0 g')

db.session.add(apple)

butternut_squash_apple_prune = Recipe(
name='Butternut Squash, Apple and Prune',
image='https://www.annabelkarmel.com/wp-content/uploads/2017/07/Butternut-Squash-Carrot-and-Apple-380x315.png',
extra_ingredients='100 g 1 medium carrot, peeled and sliced, 200 g butternut squash, peeled, deseeded and chopped,50 g 1 small dessert apple, peeled, cored and chopped, 10 g prunes, chopped',
method='1.Put the carrot and squash into a steamer and cook for 5 minutes. 2.Add the apple and prunes and continue to steam for 10 minutes, until all the ingredients are tender. 3.Blend with about 2 tablespoons of water from the steamer. s4.Serve with breast milk or formula if serving as First Foods Lunch.',
ingredients=[apple]
)
db.session.add(butternut_squash_apple_prune)


pepper = Ingredient(
name='Pepper',
image='https://target.scene7.com/is/image/Target/GUEST_7c2f5da1-86b0-41c7-83a5-a21359f82e6e?wid=488&hei=488&fmt=pjpeg',
nutrition_information=' Potassium 340 mg, Carbohydrate 9 g, Dietary fiber 1.5 g, Sugar 5 g, Protein 2 g, Vitamin A 23%, Vitamin C 404%, Calcium 1%, Iron 6%, Vitamin D 0%, Vitamin B-6 15%, Cobalamin 0%, Magnesium 6%')

db.session.add(pepper)

spiralized_vegetables_roasted_red_pepper_tomato_pesto = Recipe(
name='Spiralized Vegetables with Roasted Red Pepper & Tomato Pesto',
image='https://www.annabelkarmel.com/wp-content/uploads/2015/08/Spiralized_Vegetables_with_Roasted_Red_Pepper_and_Tomato_Pesto-3-380x315.jpg',
extra_ingredients='2 Romero red peppers, deseeded & roughly chopped,650 g cherry tomatoes, halved, 8 tbsp olive oil,3 cloves garlic,100 g pine nuts, toasted, 75 g Italian hard-style cheese, grated,30 g basil, chopped, 1/4 red chilli, deseeded & diced, 5 large courgettes, 4 large carrots, peeled',
method='1.Preheat the oven to 140 Fan. To make the pesto, put the peppers onto a baking sheet. Drizzle over 1 tbsp of oil and season. 2.Put the tomatoes onto a baking sheet. Drizzle over 1 tbsp of oil and season. 3.Put both baking sheets into the oven for 45 minutes until semi dried. Leave to cool. 4.Put the cold peppers and tomatoes into a food processor with the remaining oil, garlic, 75g of pinenuts, basil, cheese and chilli. Whiz until smooth and season. 5.Put the courgettes and carrots through a spiralizer to make long spaghetti. Heat a frying pan until hot. Add a little oil. Quickly fry the carrots for 4 – 5 minutes then add the courgettes for 2 minutes, tossing together lightly. 6.Warm the pesto and mix with the vegetables and reserved pinenuts.',
ingredients=[pepper]
)
db.session.add(spiralized_vegetables_roasted_red_pepper_tomato_pesto)


orange = Ingredient(
name='Orange',
image='https://5.imimg.com/data5/KM/QP/MY-22954806/orange-500x500.jpg',
nutrition_information=' Potassium 181 mg, Carbohydrate 12 g, Dietary fiber 2.4 g, Sugar 9 g, Protein 0.9 g, Vitamin A 4%, Vitamin C 88%, Calcium 4%, Iron 0%, Vitamin D 0%, Vitamin B-6 5%, Cobalamin 0%, Magnesium 2%')

db.session.add(orange)

chocolate_orange_shortbread = Recipe(
name='Chocolate Orange Shortbread',
image='https://www.annabelkarmel.com/wp-content/uploads/2017/06/APP-chocolate-orange-shortbread-1-380x315.jpg',
extra_ingredients='85g caster sugar, 85g semolina or 60g Polenta for a glute-free alternative, 175g plain flour or 175g gluten-free plain flour, 175g cold unsalted butter, cubed, 75g orange & milk chocolate bar, finely chopped',
method='Preheat the oven to 180⁰C/Gas 4. Line two baking sheets with non stick paper.2.Put the sugar, semolina (or polenta if using), flour & butter into a food processor.3.Whiz together until the mixture looks like breadcrumbs, then whiz a little longer until the dough just comes together.4.Tip out onto a floured surface. Add the chocolate & gently knead until the dough just comes together.5.Roll out & cut into rounds using a 6 cm round cutter. Place on the baking sheets & prick the biscuits with a fork. Bake for about 11 minutes until pale golden.6.Leave to cool, then transfer to a wire rack. Sprinkle with a little extra sugar if you like.',
ingredients=[orange]
)
db.session.add(chocolate_orange_shortbread)

cod = Ingredient(
name='Cod',
image='https://thecornishfishmonger.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/c/o/cod_fillet.jpg',
nutrition_information='Total Fat 0.7g, Saturated Fat 0.1g, Cholesterol 43mg, Sodium 54mg, Protein 18g,Vitamin A 1 %, Vitamin C 2 %, Calcium 2 %, Iron 2 %')
db.session.add(cod)

cod_couscous_balls = Recipe(
name='Cod & Couscous Balls',
image='https://www.annabelkarmel.com/wp-content/uploads/2019/02/AK-2201201900275_8357_Uncropped-380x315.jpg',
extra_ingredients='1 fillet of Cod 100g,couscous (cooked and cooled), 4 spring onions, sliced, 1 small carrot, peeled and grated, ½ apple, peeled and grated, 40g Parmesan, grated, 2 tbsp fresh basil , chopped, 1 egg yolk',
method='Measure all of the ingredients into a food processor. Whiz until finely chopped. Add the egg yolk and season lightly. Shape into 20 balls. 2.Place on a baking sheet lined with non stick paper and drizzle with a little oil. 3. Bake for 20 minutes turning over halfway through the cooking time.',
ingredients=[cod]
)
db.session.add(cod_couscous_balls)


avocado = Ingredient(
name='Avocado',
image='https://images-na.ssl-images-amazon.com/images/I/81LKLCmdAQL._SY355_.jpg',
nutrition_information='Fat 15 g, Saturated fat 2.1 g, Polyunsaturated fat 1.8 g, Monounsaturated fat 10 g, Sodium 7 mg, Potassium 485 mg, Carbohydrate 9 g, Dietary fiber 7, Sugar 0.7 g, Protein 2 g, Vitamin A 2%, Vitamin C 16%, Calcium 1%, Iron 3%, Vitamin D 0%, Vitamin B-6 15%, Cobalamin 0%, Magnesium 7%')
db.session.add(avocado)

avocado_banana_puree = Recipe(
name='Avocado & Banana Puree',
image='https://www.annabelkarmel.com/wp-content/uploads/2008/06/avocado-banana-puree-3-380x315.jpg',
extra_ingredients='1/4 avocado, 1/2 smal ripe banana, 1 or 2 tbsp baby\'s usual milk or greek yoghurt',
method='1.Mash the avocado together with the banana and the milk.2.You can also substitute the flesh of half a small papaya for the avocado. If using papaya, the milk is then optional.',
ingredients=[avocado]
)
db.session.add(avocado_banana_puree)

courgette = Ingredient(
name='Courgette',
image='https://www.planetorganic.com/images/products/large/10075.jpg',
nutrition_information='Total Fat 0.3, Saturated fat 0.1 g, Polyunsaturated fat 0.1g, Sodium 8 mg, Potassium 261 mg, Carbohydrate 3.1 g,Dietary fiber 1 g, Sugar 2.5 g, Protein 1.2 g, Vitamin A 4%, Vitamin C 29%, Calcium 1%, Iron 2%, Vitamin D 0%, Vitamin B-6 10%, Magnesium 4%'
)
db.session.add(courgette)

courgette_carrot_risotto = Recipe(
name='Courgette & Carrot Risotto',
image='https://www.annabelkarmel.com/wp-content/uploads/2009/05/Summer-Risotto-3-380x315.jpg',
extra_ingredients='900 ml vegetable stock or chicken stock, 4 large shallots or one onion, finely chopped, 1 garlic clove, crushed, 40 g butter, 1 tbsp olive oil, 40 g red pepper, chopped, 200 g arborio (risotto) rice, 75 g courgette, diced, 2 medium tomatoes, skinned, de-seeded & chopped (approx. 225 g), 4 tbsp white wine (for adult version), 40 g Italian hard style cheese, grated',
method='1.Bring the stock to the boil and allow to simmer. Heat the oil and butter in a large frying pan and sauté the shallots and garlic for 1 minute. 2.Add the red pepper and cooked for 5 minutes, stirring occasionally until softened. Add the rice and make sure that it is well coated. Stir for 1 minute. 3.Add 1 or 2 ladlefuls of hot stock and simmer, stirring, until it has been absorbed, then add another ladleful of stock. 4.Continue adding the stock a little at a time, and simmer until the rice absorbs the liquid before adding more, stirring frequently.5.After 10 minutes, add the diced courgette and tomato.6.After about 8 minutes add the white wine (for adults). When all the stock has been added and the rice is cooked (it will probably take about 20 minutes for the rice to cook through), stir in the Italian hard style cheese until melted and season to taste.',
ingredients=[courgette]
)
db.session.add(courgette_carrot_risotto)

#
# lauren = User(
# username='Lauren',
# email='lauren@bell.com',
# password_hash='password',
# avatar='https://workhound.com/wp-content/uploads/2017/05/placeholder-profile-pic.png'
# )
# db.session.add(lauren)

gessica = User(
username='Gessica',
email='gessica@mail.com',
password_hash='password1',
avatar='https://www.whatsappprofiledpimages.com/wp-content/uploads/2018/07/awesome-profile-pics-300x300.jpg'
)
db.session.add(gessica)
comment1 = Comment(content='This is a yummy recipe.', recipes=banana_carrot_seed_bread)

# lauren = User(
# name='Lauren',
# email='lauren@bell.com',
# password_hash='password',
# avatar='https://workhound.com/wp-content/uploads/2017/05/placeholder-profile-pic.png'
# )
# db.session.add(lauren)



db.session.add(comment1)

db.session.commit()
