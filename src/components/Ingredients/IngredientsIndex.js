import React from 'react'
import 'bulma'
import axios from 'axios'
import IngredientsCard from './IngredientsCard'
// import { Link } from 'react-router-dom'

class IngredientsIndex extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get('/api/ingredients')
      .then(res => this.setState({ ingredients: res.data }))
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
              <IngredientsCard {...ingredient}/>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default IngredientsIndex
