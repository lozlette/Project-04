import React from 'react'
import 'bulma'
import axios from 'axios'
import IngredientsCard from './IngredientsCard'
import Auth from '../../lib/Auth'
import _ from 'lodash'

class IngredientsIndex extends React.Component {
  constructor() {
    super()

    this.state = {
      choices: []
    }
    this.handleClick = this.handleClick.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount(){
    axios.get('/api/ingredients')
      .then(res => this.setState({ ingredients: res.data }))

    axios.get('/api/recipes',
      {headers: { Authorization: `Bearer ${Auth.getToken()}` }})
      .then(res => this.setState({ recipes: res.data }))
  }

  handleClick(e){
    if(this.state.choices.length < 2)this.state.choices.push(parseInt(e.target.id))
    console.log('CHOICE', this.state.choices)
    console.log('STATE', this.state)
  }

  handleSubmit(){
    const resultRecipes = this.state.recipes.filter(recipe => {
      const ingredientIds = recipe.ingredients.map(ingredient => ingredient.id)
      return _.intersection(ingredientIds, this.state.choices).length === 2
    })
    this.props.history.push(`/recipes/${resultRecipes[0].id}`)
    console.log(resultRecipes)
  }

  render(){
    if(!this.state.ingredients) return <h1>Loading...</h1>
    console.log(this.state.ingredients)
    return(
      <div>
        <section className="hero is-success is-small">
          <div className="hero-body">
            <div className="container">
              <h1 className="title">
                Select two ingredients:
              </h1>
              <h2 className="subtitle">
                1 that <strong>your child</strong> likes to eat & 1 that <strong>you</strong> would like your child to eat
              </h2>
            </div>
          </div>
        </section>
        <div className="columns is-multiline">
          {this.state.ingredients.map(ingredient =>
            <div className="column is-one-quarter" key={ingredient.id}>
              <button onClick={this.handleClick} className="ingredientBtn"><IngredientsCard {...ingredient}/></button>
            </div>
          )}
        </div>
        <button className="button submitingbtn is-fullwidth is-success" onClick={this.handleSubmit}>Submit</button>
      </div>
    )
  }
}

export default IngredientsIndex
