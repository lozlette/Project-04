import React from 'react'
import 'bulma'
import axios from 'axios'
import IngredientsCard from './IngredientsCard'
import { Link } from 'react-router-dom'

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
      <div className="container">
        <div className="columns is-multiline">
          {this.state.ingredients.map(ingredient =>
            <div className="column is-one-third" key={ingredient.id}>
              <Link to={`/ingredients/${ingredient.id}`}>
                <IngredientsCard {...ingredient}/>
              </Link>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default IngredientsIndex
