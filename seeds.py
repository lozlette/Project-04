from app import app, db, bcrypt
from models.ingredient import Ingredient
from models.recipe import Recipe
from models.user import User
from models.comment import Comment

with app.app_context():
    db.drop_all()
    db.create_all()

#INGREDIENTS
banana = Ingredient(
name='Banana',
image='https://images.pexels.com/photos/461208/pexels-photo-461208.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Vitamin B6 - 0.5 mg, Manganese - 0.3 mg, Vitamin C - 9 mg, Potassium - 450 mg, Dietary Fiber - 3g, Protein - 1 g, Magnesium - 34 mg, Folate - 25.0 mcg.')
db.session.add(banana)


carrot = Ingredient(
name='Carrot',
image='https://images.pexels.com/photos/143133/pexels-photo-143133.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Fiber: 2.8 g, Fat: 0.2 g, Calories: 41, Trans fat: ~')
db.session.add(carrot)


muffins = Ingredient(
name='muffins',
image='https://images.pexels.com/photos/1657343/pexels-photo-1657343.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Total Fat 16 g, Saturated fat 2.7 g, Polyunsaturated fat 7 g, Monounsaturated fat 6 g, Trans fat 0.3 g, Cholesterol 30 mg, Sodium 339 mg, Potassium 115 mg, Carbohydrate 54 g, Dietary fiber 1 g ,Sugar 33 g, Protein 4.5 g, Vitamin A 1%, Vitamin C 1%, Calcium 4%, Iron 7%, Vitamin D 1% , Cobalamin 3%, Magnesium 2%')
db.session.add(muffins)


spinach = Ingredient(
name='Spinach',
image='https://images.pexels.com/photos/1751149/pexels-photo-1751149.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Protein 2.9 g, Carbs 3.6 g, Sugar 0.4 g, Fiber 2.2 g, Fat 0.4 g, Saturated 0.06 g, Monounsaturated 0.01 g, Polyunsaturated 0.17 g, Omega-3 0.14 g ,Omega-6 0.03 g, Trans fat ~')
db.session.add(spinach)


kale = Ingredient(
name='Kale',
image='https://as2.ftcdn.net/jpg/00/64/38/81/500_F_64388152_C75t3QRNZmxQPs3R5sXIdGNEFXNWX8pZ.jpg',
nutrition_information=' 3 grams of protein, 2.5 grams of fiber, Vitamins A, C, and K, Folate, B vitamin, Alpha-linolenic acid, omega-3 fatty acid.')
db.session.add(kale)


apple = Ingredient(
name='Apple',
image='https://images.unsplash.com/photo-1501925654609-7b41cf395eb8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
nutrition_information=' Protein 0.3 g,Carbs 13.8 g, Sugar 10.4 g, Fiber 2.4 g, Fat 0.2 g, Saturated 0.03 g, Monounsaturated 0.01 g, Polyunsaturated 0.05 g, Omega-3 0.01 g, Omega-6 0.04 g, Trans fat 0 g')
db.session.add(apple)


pepper = Ingredient(
name='Pepper',
image='https://images.unsplash.com/photo-1509377244-b9820f59c12f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80',
nutrition_information=' Potassium 340 mg, Carbohydrate 9 g, Dietary fiber 1.5 g, Sugar 5 g, Protein 2 g, Vitamin A 23%, Vitamin C 404%, Calcium 1%, Iron 6%, Vitamin D 0%, Vitamin B-6 15%, Cobalamin 0%, Magnesium 6%')
db.session.add(pepper)


courgette = Ingredient(
name='Courgette',
image='https://images.pexels.com/photos/128420/pexels-photo-128420.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Total Fat 0.3, Saturated fat 0.1 g, Polyunsaturated fat 0.1g, Sodium 8 mg, Potassium 261 mg, Carbohydrate 3.1 g,Dietary fiber 1 g, Sugar 2.5 g, Protein 1.2 g, Vitamin A 4%, Vitamin C 29%, Calcium 1%, Iron 2%, Vitamin D 0%, Vitamin B-6 10%, Magnesium 4%'
)
db.session.add(courgette)


chocolate = Ingredient(
name='chocolate',
image='https://images.pexels.com/photos/1693027/pexels-photo-1693027.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Total Fat 31 g,Saturated fat 19 g, Polyunsaturated fat 1.1 g, Monounsaturated fat 10 g, Trans fat 0.1 g, Cholesterol 8 mg, Sodium 24 mg, Potassium 559 mg, Carbohydrate 61 g, Dietary fiber 7 g, Sugar 48 g, Protein 4.9 g, Caffeine 43 mg, Vitamin A 1%, Vitamin C 0%, Calcium 5%, Iron 44%, Vitamin D 0%, Vitamin B-6 0%, Cobalamin 3%, Magnesium 36%')
db.session.add(chocolate)


orange = Ingredient(
name='Orange',
image='https://images.pexels.com/photos/691166/pexels-photo-691166.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information=' Potassium 181 mg, Carbohydrate 12 g, Dietary fiber 2.4 g, Sugar 9 g, Protein 0.9 g, Vitamin A 4%, Vitamin C 88%, Calcium 4%, Iron 0%, Vitamin D 0%, Vitamin B-6 5%, Cobalamin 0%, Magnesium 2%')
db.session.add(orange)

tomatoes = Ingredient(
name='tomatoes',
image='https://images.unsplash.com/photo-1502234665511-5745ea0a6a29?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
nutrition_information='Calories 18, Water 95 %, Protein 0.9 g, Carbs 3.9 g, Sugar 2.6 g, Fiber 1.2 g, Fat 0.2 g, Saturated 0.03 g, Monounsaturated 0.03 g, Polyunsaturated 0.08 g, Omega-6 0.08 g')
db.session.add(tomatoes)


cod = Ingredient(
name='Cod',
image='https://previews.123rf.com/images/zhekos/zhekos1311/zhekos131100079/23843376-raw-cod-fish-fillet-with-lemon-slices-and-rosemary-closeup-on-wooden-background-vertical-view.jpg',
nutrition_information='Total Fat 0.7g, Saturated Fat 0.1g, Cholesterol 43mg, Sodium 54mg, Protein 18g,Vitamin A 1 %, Vitamin C 2 %, Calcium 2 %, Iron 2 %')
db.session.add(cod)


sweet_potato = Ingredient(
name='sweet potato',
image='https://images.pexels.com/photos/89247/pexels-photo-89247.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Sodium 55 mg, Potassium 337 mg, Carbohydrate 20 g, Dietary fiber 3 g, Sugar 4.2 g, Protein 1.6 g, Vitamin A 283%, Vitamin C 4%, Calcium 3%, Iron 3%, Vitamin B-6 10%, Magnesium 6%')
db.session.add(sweet_potato)


avocado = Ingredient(
name='Avocado',
image='https://images.pexels.com/photos/557659/pexels-photo-557659.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
nutrition_information='Fat 15 g, Saturated fat 2.1 g, Polyunsaturated fat 1.8 g, Monounsaturated fat 10 g, Sodium 7 mg, Potassium 485 mg, Carbohydrate 9 g, Dietary fiber 7, Sugar 0.7 g, Protein 2 g, Vitamin A 2%, Vitamin C 16%, Calcium 1%, Iron 3%, Vitamin D 0%, Vitamin B-6 15%, Cobalamin 0%, Magnesium 7%')
db.session.add(avocado)


pancake = Ingredient(
name='Pancake',
image='https://images.pexels.com/photos/357573/pexels-photo-357573.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
nutrition_information='Total Fat 3.9g , Saturated Fat 0.8g , Polyunsaturated Fat 1.8g, Monounsaturated Fat 1g, Cholesterol 24mg, Sodium 176mg, Potassium 53mg, Total Carbohydrates 11g, Protein 2.6g grams, Vitamin A 1.6%, Vitamin C 0.2% , Calcium 6.7% , Iron 4% ')
db.session.add(pancake)


blueberries = Ingredient(
name='blueberries',
image='https://images.unsplash.com/photo-1520605363242-1012f0ae0c15?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=925&q=80',
nutrition_information='3.6 g dietary fiber, or 14.4 percent of your daily value (DV), 9 milligrams (mg) calcium, 0.9 percent DV., 9 mg magnesium, 2.25 percent DV., 114 mg potassium, 2.42 percent DV., 14.4 mg vitamin C, 24 percent DV., 9 micrograms (mcg) folate, 2.25 percent DV.')
db.session.add(blueberries)


#RECIPES
banana_carrot_seed_bread = Recipe(
name='Banana, Carrot and Seed Bread',
image='https://images.unsplash.com/photo-1547033964-1be30700c397?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
extra_ingredients='150g / 5oz softened unsalted butter, 2 large eggs, 200g/ 7oz ripe bananas, peeled and mashed, 125g / 4½oz grated carrot, 25g / 1oz sultanas, 125g / 4½oz soft dark brown sugar, 225g / 8oz self-raising flour, ½ teaspoon ground cinnamon, 1 teaspoon mixed spice, 1 teaspoon ground ginger, 25g / 1oz pumpkin seeds, 25g / 1oz sunflower seeds, Butter, for spreading and greasing',
method='1.Preheat the oven to 170°C/340°F/Gas 3, grease a 900 g/2 lb loaf tin and line it with baking parchment.2.Place all of the ingredients, except the topping, in a large mixing bowl. Whisk together with an electric hand-held whisk for 1–2 minutes until light and fluffy. Alternatively, use a stand mixer fitted with the paddle or whisk attachment. 3.Spoon the mixture into the tin and level out the top. 4.Sprinkle with the extra seeds and bake for 1–1¼ hours until golden, well risen and a skewer inserted comes out clean. 5.Remove from the oven and leave to cool on a wire rack, then remove from the tin. Dust with icing sugar (if using), cut into slices, spread with butter and serve.',
ingredients=[banana, carrot]
)
db.session.add(banana_carrot_seed_bread)


carrot_cheese_muffins = Recipe(
name='Carrot & Cheese Muffins',
image='https://images.unsplash.com/photo-1548693563-25dc13e7b2c1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
extra_ingredients='2 eggs, 175g self raising flour, 1 tsp baking powder, 100 ml milk,100g carrot, peeled and grated, 3 tbsp sunflower oil,1 tbsp chives, chopped,6 spring onions, sliced,1 tbsp fresh basil , chopped,50g parmesan, grated',
method='1.Preheat the oven to 180C Fan. Line a muffin tin with 10 muffin cases.2.Whisk the egg, flour, baking powder, milk and oil together in a large bowl. Add the carrot, herbs, spring onion and cheese and fold together. Spoon into the cases.3.Bake in the oven for 18 minutes until sell risen and lightly golden brown.',
ingredients=[carrot, muffins]
)
db.session.add(carrot_cheese_muffins)


cod_broccoli_spinach_puree = Recipe(
name='Cod, Broccoli & Spinach Puree',
image='https://www.annabelkarmel.com/wp-content/uploads/2016/10/Salmon_Broccoli_Puree-lowres-2-380x315.jpg',
extra_ingredients='A knob of butter,100g shallots, sliced,225g peeled potatoes, diced,300 ml water,225g cod fillet, diced, 100g broccoli florets, 30g baby spinach, 75ml milk, 15g parmesan cheese, grated, A squeeze of lemon juice',
method='1.Melt the butter in a saucepan. Add the shallots and potatoes and fry for 2 minutes. Add the water, cover with a lid and simmer for 10 minutes. 2.Add the cod and broccoli and cover and simmer for another 10 minutes until the vegetables are cooked through. Add the spinach two minutes before the end of the cooking time. 3.Add the milk and parmesan cheese. 4.Blend until smooth using an electric hand blender and the lemon juice.',
ingredients=[spinach, cod]
)
db.session.add(cod_broccoli_spinach_puree)


sweet_potato_kale_croquettes = Recipe(
name='Sweet Potato and Kale Croquettes',
image='https://www.thespruceeats.com/thmb/5QGgbDoHWwNcsG6hP3anCEGlG_8=/4288x2848/filters:no_upscale():max_bytes(150000):strip_icc()/coxinha-brazilian-chicken-croquettes-3029668-Hero-5b7d5f9546e0fb00252abc5f.jpg',
extra_ingredients='2 tbsp sunﬂower oil, 1 small onion, chopped, 100g (31/2oz) mushrooms, chopped, 1 medium carrot, grated, 20g (3/4oz) kale, chopped, 1 garlic clove, crushed, 150g (5 1/2oz) baking potato, pricked, 150g (5 1/2oz) sweet potato, pricked, 50g (1 3/4oz) fresh breadcrumbs or wheat or gluten-free breadcrumbs, 30g (1oz) Cheddar cheese or dairy-free alternative, grated, Plain ﬂour or gluten-free ﬂour, to coat',
method='Heat 1 tablespoon of the oil in a frying pan. Add the onion, mushrooms, carrot, kale, and garlic, and fry for 5 minutes over a medium heat. Leave to cool. 2.Cook the potatoes in a microwave for 10 minutes until soft. Leave to cool, then scoop out the potato ﬂesh into a bowl. 3. Add the cooked vegetables, breadcrumbs, and cheese and mix together until blended. Shape into 14 small croquettes and roll in the ﬂour. 4.Heat the remaining 1 tablespoon of oil in a frying pan. Fry the croquettes for 3–4 minutes, until golden on all sides and cooked through. Drain on kitchen paper and leave to cool before serving. 5.When needed, thaw overnight in the fridge or leave out for a few hours at room temperature. Reheat in an oven preheated to 180ºC (fan 160ºC), gas 4 for 10–12 minutes.',
ingredients=[kale, sweet_potato],
)
db.session.add(sweet_potato_kale_croquettes)


butternut_squash_apple_prune = Recipe(
name='Butternut Squash, Apple and Prune',
image='https://www.annabelkarmel.com/wp-content/uploads/2017/07/Butternut-Squash-Carrot-and-Apple-380x315.png',
extra_ingredients='100 g 1 medium carrot, peeled and sliced, 200 g butternut squash, peeled, deseeded and chopped,50 g 1 small dessert apple, peeled, cored and chopped, 10 g prunes, chopped',
method='1.Put the carrot and squash into a steamer and cook for 5 minutes. 2.Add the apple and prunes and continue to steam for 10 minutes, until all the ingredients are tender. 3.Blend with about 2 tablespoons of water from the steamer. s4.Serve with breast milk or formula if serving as First Foods Lunch.',
ingredients=[apple]
)
db.session.add(butternut_squash_apple_prune)


spiralized_vegetables_roasted_red_pepper_tomato_pesto = Recipe(
name='Spiralized Vegetables with Roasted Red Pepper & Tomato Pesto',
image='https://www.annabelkarmel.com/wp-content/uploads/2015/08/Spiralized_Vegetables_with_Roasted_Red_Pepper_and_Tomato_Pesto-3-380x315.jpg',
extra_ingredients='2 Romero red peppers, deseeded & roughly chopped,650 g cherry tomatoes, halved, 8 tbsp olive oil,3 cloves garlic,100 g pine nuts, toasted, 75 g Italian hard-style cheese, grated,30 g basil, chopped, 1/4 red chilli, deseeded & diced, 5 large courgettes, 4 large carrots, peeled',
method='1.Preheat the oven to 140 Fan. To make the pesto, put the peppers onto a baking sheet. Drizzle over 1 tbsp of oil and season. 2.Put the tomatoes onto a baking sheet. Drizzle over 1 tbsp of oil and season. 3.Put both baking sheets into the oven for 45 minutes until semi dried. Leave to cool. 4.Put the cold peppers and tomatoes into a food processor with the remaining oil, garlic, 75g of pinenuts, basil, cheese and chilli. Whiz until smooth and season. 5.Put the courgettes and carrots through a spiralizer to make long spaghetti. Heat a frying pan until hot. Add a little oil. Quickly fry the carrots for 4 – 5 minutes then add the courgettes for 2 minutes, tossing together lightly. 6.Warm the pesto and mix with the vegetables and reserved pinenuts.',
ingredients=[pepper]
)
db.session.add(spiralized_vegetables_roasted_red_pepper_tomato_pesto)


chocolate_orange_shortbread = Recipe(
name='Chocolate Orange Shortbread',
image='https://www.annabelkarmel.com/wp-content/uploads/2017/06/APP-chocolate-orange-shortbread-1-380x315.jpg',
extra_ingredients='85g caster sugar, 85g semolina or 60g Polenta for a glute-free alternative, 175g plain flour or 175g gluten-free plain flour, 175g cold unsalted butter, cubed, 75g orange & milk chocolate bar, finely chopped',
method='Preheat the oven to 180⁰C/Gas 4. Line two baking sheets with non stick paper.2.Put the sugar, semolina (or polenta if using), flour & butter into a food processor.3.Whiz together until the mixture looks like breadcrumbs, then whiz a little longer until the dough just comes together.4.Tip out onto a floured surface. Add the chocolate & gently knead until the dough just comes together.5.Roll out & cut into rounds using a 6 cm round cutter. Place on the baking sheets & prick the biscuits with a fork. Bake for about 11 minutes until pale golden.6.Leave to cool, then transfer to a wire rack. Sprinkle with a little extra sugar if you like.',
ingredients=[orange,chocolate]
)
db.session.add(chocolate_orange_shortbread)


cod_couscous_balls = Recipe(
name='Cod & Couscous Balls',
image='https://www.annabelkarmel.com/wp-content/uploads/2019/02/AK-2201201900275_8357_Uncropped-380x315.jpg',
extra_ingredients='1 fillet of Cod 100g,couscous (cooked and cooled), 4 spring onions, sliced, 1 small carrot, peeled and grated, ½ apple, peeled and grated, 40g Parmesan, grated, 2 tbsp fresh basil , chopped, 1 egg yolk',
method='Measure all of the ingredients into a food processor. Whiz until finely chopped. Add the egg yolk and season lightly. Shape into 20 balls. 2.Place on a baking sheet lined with non stick paper and drizzle with a little oil. 3. Bake for 20 minutes turning over halfway through the cooking time.',
ingredients=[cod]
)
db.session.add(cod_couscous_balls)


avocado_banana_puree = Recipe(
name='Avocado & Banana Puree',
image='https://www.annabelkarmel.com/wp-content/uploads/2008/06/avocado-banana-puree-3-380x315.jpg',
extra_ingredients='1/4 avocado, 1/2 smal ripe banana, 1 or 2 tbsp baby\'s usual milk or greek yoghurt',
method='1.Mash the avocado together with the banana and the milk.2.You can also substitute the flesh of half a small papaya for the avocado. If using papaya, the milk is then optional.',
ingredients=[avocado, banana]
)
db.session.add(avocado_banana_puree)


courgette_carrot_risotto = Recipe(
name='Courgette & Carrot Risotto',
image='https://images.unsplash.com/photo-1476124369491-e7addf5db371?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
extra_ingredients='900 ml vegetable stock or chicken stock, 4 large shallots or one onion, finely chopped, 1 garlic clove, crushed, 40 g butter, 1 tbsp olive oil, 40 g red pepper, chopped, 200 g arborio (risotto) rice, 75 g courgette, diced, 2 medium tomatoes, skinned, de-seeded & chopped (approx. 225 g), 4 tbsp white wine (for adult version), 40 g Italian hard style cheese, grated',
method='1.Bring the stock to the boil and allow to simmer. Heat the oil and butter in a large frying pan and sauté the shallots and garlic for 1 minute. 2.Add the red pepper and cooked for 5 minutes, stirring occasionally until softened. Add the rice and make sure that it is well coated. Stir for 1 minute. 3.Add 1 or 2 ladlefuls of hot stock and simmer, stirring, until it has been absorbed, then add another ladleful of stock. 4.Continue adding the stock a little at a time, and simmer until the rice absorbs the liquid before adding more, stirring frequently.5.After 10 minutes, add the diced courgette and tomato.6.After about 8 minutes add the white wine (for adults). When all the stock has been added and the rice is cooked (it will probably take about 20 minutes for the rice to cook through), stir in the Italian hard style cheese until melted and season to taste.',
ingredients=[courgette, carrot]
)
db.session.add(courgette_carrot_risotto)


blueberry_pancakes = Recipe(
name='American Style Blueberry Pancakes',
image='https://images.pexels.com/photos/821403/pexels-photo-821403.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
extra_ingredients='150 g plain flour, 2 tbsp granulated sugar, 1 tsp baking powder, 1/2 tsp bicarbonate of soda, 1 large pinch of salt, 250 ml buttermilk or 120 g plain yoghurt plus, 120 ml milk, 1 egg, 1/4 tsp vanilla extract, 200 g blueberries, sunflower oil for greasing, 2 tbsp maple syrup',
method='1.Put the flour, sugar, bicarbonate of soda, baking powder and salt in a bowl. Add half the buttermilk, the egg and vanilla extract. 2.Whisk everything together to make a batter. Add the remaining buttermilk and whisk until smooth. 3.Add the blueberries and mix them into the batter gently. Try not to squash them. 4.Lightly oil and heat a non-stick frying pan. Drop in 2 tbsp batter per pancake. Cook for 1 ½ – 2 minutes, until golden underneath and bubbling on top. 5.Flip over and cook for a further 1 to 2 minutes. Serve with maple syrup.',
ingredients=[pancake, blueberries]
)
db.session.add(blueberry_pancakes)


blueberry_pear_banana_puree = Recipe(
name='Blueberry, Pear & Banana Puree',
image='https://www.annabelkarmel.com/wp-content/uploads/2014/06/Blueberry-Pear-and-Banana-Puree-3-380x315.jpg',
extra_ingredients='2 pears, peeled & diced, 150 g bluberries, 1 banana, sliced',
method='1.Put the pears and blueberries into a saucepan. Simmer for 5 minutes until soft. 2.Add the banana and blend until smooth or to your desired consistency.',
ingredients=[banana, blueberries]
)
db.session.add(blueberry_pear_banana_puree)


chocolate_chip_kale_cookies = Recipe(
name='Chocolate Chip Kale Cookies',
image='https://images.unsplash.com/photo-1497051788611-2c64812349fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=714&q=80',
extra_ingredients='1 cup spelt, white, or oat flour, loosely packed (125g), 1/2 tsp baking soda,1/4 tsp salt, 1/2 cup unrefined sugar or xylitol,1/3 cup chocolate chips, 2 tbsp milk of choice, 2 tbsp oil (24g), 1/4 tsp pure vanilla extract, 1 cup raw kale or spinach, no stems',
method='1 Preheat oven to 325 F. 2.Process kale or dice it extremely fine. 3. Combine all dry ingredients except kale in a medium bowl, then stir in remaining ingredients to form a dough. It will be dry at first, so keep stirring until a cookie-dough texture is achieved. (Add 1 additional tbsp milk of choice only if needed – I didn’t need it.) 4.Roll into balls. 5.Place on a cookie tray, and bake 11 minutes. 6.They will look underdone. 7.Remove from the oven anyway, and let them cool 10 minutes, during which time they will firm up. You can also make extra cookie dough balls and freeze them to bake at a later date.',
ingredients=[chocolate, kale]
)
db.session.add(chocolate_chip_kale_cookies)


cod_tomato_sauce = Recipe(
name='Cod with Hearty Tomato Sauce',
image='https://images.pexels.com/photos/1516415/pexels-photo-1516415.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
extra_ingredients='2 cans (14-1/2 ounces each) diced tomatoes with basil, oregano and garlic, undrained, 4 cod fillets (6 ounces each), 2 tablespoons olive oil, divided, 2 medium onions, halved and thinly sliced (about 1-1/2 cups), 1/2 teaspoon dried oregano, 1/4 teaspoon pepper, 1/4 teaspoon crushed red pepper flakes, Hot cooked whole wheat pasta, Minced fresh parsley, optional',
method='1.Place tomatoes in a blender. Cover and process until pureed. 2.Pat fish dry with paper towels. In a large skillet, heat 1 tablespoon oil over medium-high heat. Add cod fillets; cook until surface of fish begins to color, 2-4 minutes on each side. Remove from pan. 3.In same skillet, heat remaining oil over medium-high heat. Add onions; cook and stir until tender, 2-4 minutes. Stir in seasonings and pureed tomatoes; bring to a boil. Add cod; return just to a boil, spooning sauce over tops. Reduce heat; simmer, uncovered, until fish just begins to flake easily with a fork, 5-7 minutes. Serve with pasta. If desired, sprinkle with parsley.',
ingredients=[cod, tomatoes]
)
db.session.add(cod_tomato_sauce)


sweet_potato_muffins = Recipe(
name='Sweet Potato Muffins',
image='https://images.unsplash.com/photo-1487124504955-e42a39e11aaf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1012&q=80',
extra_ingredients='3 cups of mashed sweet potato, 2 cups flour, 2 tsp cinnamon, 1 tsp baking soda, 1/4 tsp baking powder, 1/2 tsp salt, 1 cup sugar, 3/4 cup vegetable oil, 3 large eggs, 1 tsp vanilla, 1/2 cup ground flaxseed meal optional',
method='1.Put the pears and blueberries into a saucepan. Simmer for 5 minutes until soft. 2.Add the banana and blend until smooth or to your desired consistency.',
ingredients=[muffins, sweet_potato]
)
db.session.add(sweet_potato_muffins)



#BANANA COMBINATIONS
apple_banana_cake_bread = Recipe(
name='Easy apple banana cake bread',
image='https://images-gmi-pmc.edge-generalmills.com/f2381a0e-7aff-45a7-be6b-527fbf1ba28e.jpg',
extra_ingredients='2 cups flour, 3/4 teaspoon baking soda, 1/8 teaspoon salt, 2 teaspoons cinnamon, 2 bananas , mashed, 1/2 cup sugar, 1/4 cup brown sugar, 1/3 cup sour cream, 1/4 cup vegetable oil, 2 eggs, 2 teaspoons vanilla, 1/2 cup diced apple, skins removed, 1/2 banana, sliced thin for garnish',
method='1.Preheat oven to 350 and prepare 9×5 inch loaf pan, cake pan, OR tarte pan with parchment paper or grease it generously. 2.In one large bowl mix flour, baking soda, salt and cinnamon. 3.In another large bowl mix together banana, sugar, brown sugar, sour cream, oil, eggs and vanilla. 4.Add wet mixture to the flour mixture and stir well till all is incorporated. 5.Stir in apples and mix to evenly distribute. 6.Pour into pan. 7.Lay thin sliced bananas on top to caramelize as bread bakes. 8.Bake for 1 hour and 10 minutes, until golden brown and a stick inserted in the middle comes out clean. 9.Cool before removing from pan.',
ingredients=[banana, apple]
)
db.session.add(apple_banana_cake_bread)

spinach_banana_smoothie = Recipe(
name='Spinach and banana smoothie',
image='https://images.unsplash.com/photo-1545018595-b770da5d9e42?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1049&q=80',
extra_ingredients='250ml soya milk, 20g fresh spinach leaves, or more to taste, 1 large banana, sliced',
method='Blend soya milk and spinach leaves together in a blender until smooth. 2.Add banana and pulse until thoroughly blended.',
ingredients=[spinach, banana]
)
db.session.add(spinach_banana_smoothie)

banana_kiwi_kale_smoothie = Recipe(
name='Banana, Kiwi and Kale Smoothie',
image='https://diethood.com/wp-content/uploads/2014/03/Kale-Smoothie.jpg',
extra_ingredients='2 very ripe bananas, 2 kiwis , peeled and sliced in half, 1 cup kale , washed and tightly packed, 1 cup milk, 2 to 3 tablespoons honey, 1/2 cup ice',
method='1.Combine all ingredients into your blender. 2.Blend on full strength until thoroughly incorporated and smooth. 3.Pour into glasses and serve.',
ingredients=[banana, kale]
)
db.session.add(banana_kiwi_kale_smoothie)

chocolate_orange_banana_bread = Recipe(
name='Chocolate, orange and banana bread',
image='https://media.bakingmad.com/app_/responsive/BakingMad/media/content/Recipes/Cakes/Apple-Crumble-Loaf-Cake/1-Apple-Crumble-Cake-WEB.jpg?w=640',
extra_ingredients='275g / 1.75 cups plain or all purpose flour (can be gluten free), 1 tsp baking powder, 3/4 tsp baking soda, 2 medium ripe bananas, mashed, 75g / 0.3 cup coconut oil or butter, melted, 70g / 0.3 cup honey, 50g / 0.25 cup plain yogurt, 1 medium egg, 2 tsp vanilla extract, 1 orange, 75g /0.5 cup chocolate chips',
method='1.Preheat the oven to 180c/350f. Grease and line a 2lb baking tin with parchment paper. 2.Add the flour, baking soda and baking powder to a large bowl and mix with a spoon. 3.In another bowl add the mashed banana, coconut oil or butter, honey, yogurt, egg and vanilla extract and mix well with a spoon. 4.Add the zest and juice of the whole orange and mix again. 5.Add the wet ingredients to the dry ingredients and mix with a spoon just enough until all the ingredients have combined.6.Finally stir in the chocolate chips. 7.Pour the mixture into the prepared tin and bake in the oven for 30 minutes. Remove, cover loosely with tin foil (this will stop the top of the bread getting too brown) and then return to the oven for another 20-25 minutes until the bread is cooked through and a skewer inserted in the middle comes out dry. 8.Once the loaf has cooked, remove it from the oven. Allow to cool in the tin for 5-10 minutes before transferring to a wire rack to cool completely.',
ingredients=[banana, chocolate]
)
db.session.add(chocolate_orange_banana_bread)

orange_banana_date_oatmeal = Recipe(
name='Orange Banana Date Oatmeal',
image='https://images.unsplash.com/photo-1517777596324-5df4025800f2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1051&q=80',
extra_ingredients='2 cups Tropicana Pure Premium® orange juice, 1 cup water, 1/4 teaspoon salt (optional), 1/8 teaspoon ground nutmeg, 1-1/2 cups Quaker® Oats (quick or old fashioned, uncooked), 3/4 cup chopped dates or raisins, 1 medium-size ripe banana, mashed',
method='1.In medium saucepan, bring juice, water, salt and nutmeg to a boil. 2. Stir in oats and dates. 3.Return to a boil; reduce heat. 4.Cook 1 minute for quick oats or 5 minutes for old fashioned oats or until most of liquid is absorbed, stirring occasionally. 5.Stir in banana. 6.Let stand until of desired consistency.',
ingredients=[banana, orange]
)
db.session.add(orange_banana_date_oatmeal)

banana_zucchini_wholemeal_muffins = Recipe(
name='Banana Zucchini Wholemeal Muffins',
image='https://images.unsplash.com/photo-1551007796-26dd82e6175d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
extra_ingredients='1 medium banana 160g, 2 eggs, ¾ cup milk, 1/4  cup oil, 1 tsp vanilla, 3 Tbsp maple syrup or honey, 2 zucchini approx 250g, 2 cups wholemeal flour, 3 teaspoon baking powder, 1/3 cup choc chips',
method='1.Preheat your oven to 180 degrees Celsius and prepare a muffin tin. ( you will either need to grease it well or line with muffin liners. 2.In a large bowl mash a banana, add eggs, milk, oil, vanilla and maple syrup and mix well so that the eggs and liquids are well combined. 3.Peel and grate the zucchini. 4.Over a sink squeeze the grated zucchini to remove excess moisture, add the grated zucchini to the wet ingredients. 5.Add the wholemeal flour and baking powder to the bowl, I sprinkle the baking powder over the flour as I am too lazy to sift. 6.Mix, but not too well, the general rule is to not over mix a muffin, add the choc chips (reserve a few to sprinkle on the top) and again just mix gently. 7.Portion into a  12 regular muffin tray, top with a few of the reserved choc chips (just so the picky eater will definitely see them. 8.Bake at 180 degrees Celsius for 25- 30 minutes or until golden',
ingredients=[banana, courgette]
)
db.session.add(banana_zucchini_wholemeal_muffins)

banana_blender_pancakes = Recipe(
name='Banana Blender Pancakes',
image='https://mykidslickthebowl.com/wp-content/uploads/2018/03/banana-blender-pancakes-nutribullet-recipes-4-of-2017.jpg',
extra_ingredients='150 g Banana (1-2), 1/2 Cup Greek style yoghurt (140g), 1 Egg, 1 Cup rolled oats, 1 Tbsp maple syrup or honey, 1 tsp cinnamon, 1 tsp Vanilla essence, Butter/oil to grease pan',
method='1.Put all ingredients in blender and whizz until smooth batter. 2.Pour batter into a lightly greased pan on medium heat (works best as mini pancakes). 3.Wait for bubbles to appear on the surface and then flip. 4.Cook until golden on both sides. 5.Serve',
ingredients=[banana, pancake]
)
db.session.add(banana_blender_pancakes)

banana_muffins = Recipe(
name='Banana Muffins',
image='https://images.unsplash.com/photo-1519869491916-8ca6f615d6bd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80',
extra_ingredients='1 cup – almond milk, unsweetened, 2 large – egg, 1/2 cup – sugar, 3 medium – banana, 2 tablespoon – coconut oil, 2 teaspoon – vanilla extract, 1 teaspoon – cinnamon, 1 1/4 cup – flour, whole wheat, 1/2 cup – flour, all-purpose, 1 1/4 teaspoon – baking powder, 1/2 teaspoon – baking soda, 1/4 teaspoon – salt',
method='1.Preheat oven to 400 degrees F. Add 18 liners to muffin tins. Set aside. 2.Mix almond milk, eggs, sugar, bananas, coconut oil and vanilla in a blender until smooth. 3.In a large mixing bowl, stir together cinnamon, flours, baking powder, baking soda and salt. Make a well in the middle of the flour and pour in the wet ingredients while gently mixing together. Stir just until combined. 4.Pour batter into muffin cups filling 3/4 full. 5.Bake for 15-18 minutes or until a toothpick inserted comes out clean. Allow to cool for 5 minutes before serving.',
ingredients=[banana, muffins]
)
db.session.add(banana_muffins)

banana_sweet_potato_mini_cakes = Recipe(
name='Banana Sweet Potato Mini Cakes',
image='https://images.unsplash.com/photo-1508737523220-e22aa75d0d33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80',
extra_ingredients='1 banana, 1 cup chopped sweet potato, 50g butter, softened, 1 egg, 1 cup self raising flour',
method='1.Boil or steam sweet potato until tender. 2.Preheat oven to 180 C (355 F) and line a baking tray with baking paper. 3.In a large bowl, mash banana, sweet potato and softened butter together until well mashed and combined. 4.Whisk the egg in a small bowl or cup to break up the yolk, then add it to the mixing bowl and mix it through. 5.Add flour and mix until well combined. 6.Drop spoonfuls of the mixture onto the prepared baking tray, evenly spaced. 7.Bake for 14-15 minutes, until firm.',
ingredients=[banana, sweet_potato]
)
db.session.add(banana_sweet_potato_mini_cakes)


#USERS AND COMMENTS
lauren = User(
username='Lauren',
email='lauren@bell.com',
password_hash=bcrypt.generate_password_hash('password').decode('utf-8'),
avatar='https://workhound.com/wp-content/uploads/2017/05/placeholder-profile-pic.png'
)
db.session.add(lauren)
comment2 = Comment(content='This is an unusual combination but very nices.', recipe=carrot_cheese_muffins, user=lauren)
db.session.add(comment2)
comment7 = Comment(content='A great way to introduce fish into my young one\'s diet.', recipe=cod_tomato_sauce, user=lauren)
db.session.add(comment7)
comment10 = Comment(content='Delicious. First time I used my spiralizer. It made a bit of a mess in the kitchen but was lots of fun. Thanks.', recipe=spiralized_vegetables_roasted_red_pepper_tomato_pesto, user=lauren)
db.session.add(comment10)
comment14 = Comment(content='I’ve made apple cakes and I’ve made banana cakes. But I’ve never considered combining the two. This looks great!', recipe=apple_banana_cake_bread, user=lauren)
db.session.add(comment14)
comment21 = Comment(content='Could you replace the almond milk with regular milk or coconut milk?', recipe=banana_muffins, user=lauren)
db.session.add(comment21)



gessica = User(
username='Gessica',
email='g@mail.com',
password_hash=bcrypt.generate_password_hash('password1').decode('utf-8'),
avatar='https://www.whatsappprofiledpimages.com/wp-content/uploads/2018/07/awesome-profile-pics-300x300.jpg'
)
db.session.add(gessica)
comment1 = Comment(content='This is a yummy recipe.', recipe=banana_carrot_seed_bread, user=gessica)
db.session.add(comment1)
comment6 = Comment(content='I found this recipe to be a bit too sweet.', recipe=sweet_potato_muffins, user=gessica)
db.session.add(comment6)
comment11 = Comment(content='This is one creamy and yummy puree', recipe=avocado_banana_puree, user=gessica)
db.session.add(comment11)
comment15 = Comment(content='Strong banana flavour and quite sweet. I used milk instead.', recipe=spinach_banana_smoothie, user=gessica)
db.session.add(comment15)
comment20 = Comment(content='My kids are huge pancake fans, I love pancakes that have wholesome ingredients, particularly oats', recipe=banana_blender_pancakes, user=gessica)
db.session.add(comment20)


lisa = User(
username='Lisa',
email='lisa@mail.com',
password_hash=bcrypt.generate_password_hash('password2').decode('utf-8'),
avatar='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWfy52m6Vuo_i2sSV5uDIxuiLHBBIbfNjQsFnSiacsLxh81mw9'
)
db.session.add(lisa)
comment3 = Comment(content='A good way of introducing spinach to my 18 months old.', recipe=cod_broccoli_spinach_puree, user=lisa)
db.session.add(comment3)
comment12 = Comment(content='Very tasty, but the courgette need longer to cook, you have to add them before.', recipe=courgette_carrot_risotto, user=lisa)
db.session.add(comment12)
comment16 = Comment(content='The Kale smoothie was awesome. Next time going to use less honey than the max mentioned. I didn’t need all that sweetness.', recipe=banana_kiwi_kale_smoothie, user=lisa)
db.session.add(comment16)
comment19 = Comment(content='My 2-year-olds are devouring these gorgeous muffins in hushed silence!! I even forgot to peel the zucchini.', recipe=banana_zucchini_wholemeal_muffins, user=lisa)
db.session.add(comment19)


mary = User(
username='Mary',
email='mary@mail.com',
password_hash=bcrypt.generate_password_hash('password3').decode('utf-8'),
avatar='https://image.flaticon.com/icons/svg/194/194934.svg'
)
db.session.add(mary)
comment13 = Comment(content='Very good pancakes, so light. Thanks for a great recipe,', recipe=blueberry_pancakes, user=lisa)
db.session.add(comment13)
comment17 = Comment(content='This chocolate orange banana bread is absolutely delicious! Thank you so much for sharing this recipe!,', recipe=chocolate_orange_banana_bread, user=lisa)
db.session.add(comment17)
comment18 = Comment(content='This looks really nice but can I cook the oatmeal in the microwave instead?', recipe=orange_banana_date_oatmeal, user=lisa)
db.session.add(comment18)

#CONVERSATIONS BETWEEN 2 USERS
comment4 = Comment(content='As delicious as this looks and sounds, I don\'t think my Oscar is quite ready for fried food yet. Maybe in 3 months time.', recipe=sweet_potato_kale_croquettes, user=lisa)
comment5 = Comment(content='I made this last week and it was a hit with my twins', recipe=sweet_potato_kale_croquettes, user=mary)
db.session.add(comment4)
db.session.add(comment5)

comment8 = Comment(content='OMG how fun! I don’t know if I could convince my kids to eat them, but it’s a cool idea =)', recipe=chocolate_chip_kale_cookies, user=gessica)
comment9 = Comment(content='Another fun way to get green in your baked goods – Use sunflower seed butter and baking powder!', recipe=chocolate_chip_kale_cookies, user=lauren)
db.session.add(comment8)
db.session.add(comment9)



db.session.commit()
