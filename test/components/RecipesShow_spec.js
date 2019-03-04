/* global describe, it,before, after, beforeEach*/

import React from 'react'
import Promise from 'bluebird'
import axios from 'axios'
import sinon from 'sinon'
import { expect } from 'chai'
import { mount } from 'enzyme'
import { MemoryRouter, Route } from 'react-router-dom'
import RecipesShow from '../../src/components/Recipes/RecipesShow'

describe('RecipesShow tests', () =>{
  let wrapper, response

  before(done =>{
    response = Promise.resolve({
      data: {
        id: 1,
        name: 'Banana, Carrot and Seed Bread',
        image: 'https://images.unsplash.com/photo-1547033964-1be30700c397?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
        ingredients: [{
          id: 1,
          name: 'Banana',
          image: 'https://images.pexels.com/photos/461208/pexels-photo-461208.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
          nutrition_information: 'Vitamin B6 - 0.5 mg, Manganese - 0.3 mg, Vitamin C - 9 mg, Potassium - 450 mg, Dietary Fiber - 3g, Protein - 1 g, Magnesium - 34 mg, Folate - 25.0 mcg.'
        }, {
          id: 2,
          name: 'Carrot',
          image: 'https://images.pexels.com/photos/143133/pexels-photo-143133.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
          nutrition_information: 'Fiber: 2.8 g, Fat: 0.2 g, Calories: 41, Trans fat: ~'
        }],
        extra_ingredients: '150g / 5oz softened unsalted butter, 2 large eggs, 200g/ 7oz ripe bananas, peeled and mashed, 125g / 4½oz grated carrot, 25g / 1oz sultanas, 125g / 4½oz soft dark brown sugar, 225g / 8oz self-raising flour, ½ teaspoon ground cinnamon, 1 teaspoon mixed spice, 1 teaspoon ground ginger, 25g / 1oz pumpkin seeds, 25g / 1oz sunflower seeds, Butter, for spreading and greasing',
        method: '1.Preheat the oven to 170°C/340°F/Gas 3, grease a 900 g/2 lb loaf tin and line it with baking parchment.2.Place all of the ingredients, except the topping, in a large mixing bowl. Whisk together with an electric hand-held whisk for 1–2 minutes until light and fluffy. Alternatively, use a stand mixer fitted with the paddle or whisk attachment. 3.Spoon the mixture into the tin and level out the top. 4.Sprinkle with the extra seeds and bake for 1–1¼ hours until golden, well risen and a skewer inserted comes out clean. 5.Remove from the oven and leave to cool on a wire rack, then remove from the tin. Dust with icing sugar (if using), cut into slices, spread with butter and serve.',
        comments: [{
          content: 'This is a yummy recipe.',
          id: 6,
          user: {
            avatar: 'https://www.whatsappprofiledpimages.com/wp-content/uploads/2018/07/awesome-profile-pics-300x300.jpg',
            email: 'g@mail.com',
            id: 2,
            username: 'Gessica'
          }
        }]
      }
    })

    sinon.stub(axios, 'get').returns(response)
    done()
  })
  after(done=>{
    axios.get.restore()
    done()
  })
  beforeEach(done =>{
    wrapper = mount(
      <MemoryRouter initialEntries={['/recipes/1']}>
        <Route path="/recipes/:id" component={RecipesShow} />
      </MemoryRouter>
    )
    done()
  })

  it('should render the correct HTML in receipies', done =>{
    response.then(()=>{
      wrapper.update()
      // console.log(wrapper.find('.wrapper .hero .hero-body .container .title').text().debug())
      expect(wrapper.find('.wrapper .hero .hero-body .container .title').text()).to.eq('Banana, Carrot and Seed Bread')
      expect(wrapper.find('figure.image img').prop('src')).to.eq('https://images.unsplash.com/photo-1547033964-1be30700c397?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80')
      expect(wrapper.find('article').contains(<p>Fiber: 2.8 g, Fat: 0.2 g, Calories: 41, Trans fat: ~</p>))
      expect(wrapper.find('.tile .title .subtitle4').contains(<p>150g / 5oz softened unsalted butter, 2 large eggs, 200g/ 7oz ripe bananas, peeled and mashed, 125g / 4½oz grated carrot, 25g / 1oz sultanas, 125g / 4½oz soft dark brown sugar, 225g / 8oz self-raising flour, ½ teaspoon ground cinnamon, 1 teaspoon mixed spice, 1 teaspoon ground ginger, 25g / 1oz pumpkin seeds, 25g / 1oz sunflower seeds, Butter, for spreading and greasing</p>))
      expect(wrapper.find('.tile .title .subtitle5').contains(<p>1.Preheat the oven to 170°C/340°F/Gas 3, grease a 900 g/2 lb loaf tin and line it with baking parchment.2.Place all of the ingredients, except the topping, in a large mixing bowl. Whisk together with an electric hand-held whisk for 1–2 minutes until light and fluffy. Alternatively, use a stand mixer fitted with the paddle or whisk attachment. 3.Spoon the mixture into the tin and level out the top. 4.Sprinkle with the extra seeds and bake for 1–1¼ hours until golden, well risen and a skewer inserted comes out clean. 5.Remove from the oven and leave to cool on a wire rack, then remove from the tin. Dust with icing sugar (if using), cut into slices, spread with butter and serve.</p>))
      expect(wrapper.find('div.column:last-child').contains(<h2>This is a yummy recipe.</h2>))

      done()
    })
  })
})
