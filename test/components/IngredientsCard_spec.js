/* global describe, it, beforeEach*/

import React from 'react'
import {expect} from 'chai'
import {shallow} from 'enzyme'
import IngredientsCard from '../../src/components/Ingredients/IngredientsCard'

describe('IngredientsCard tests', ()=> {

  let wrapper
  beforeEach(done =>{
    const props ={
      _id: 1 ,
      name: 'Banana',
      image: 'https://images.pexels.com/photos/461208/pexels-photo-461208.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
    }
    wrapper = shallow(<IngredientsCard {...props} />)
    done()
  })

  it('should render the correct HTML', done =>{
    expect(wrapper.find('.image').length).to.eq(1)
    done()
  })
  it('should render the correct data', done =>{
    expect(wrapper.find('.image').length).to.eq(1)
    expect(wrapper.find('.image').prop('style').backgroundImage).to.eq('url(https://images.pexels.com/photos/461208/pexels-photo-461208.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)')
    expect(wrapper.find('.image').contains(<span>Banana</span>))
    done()
  })
})
