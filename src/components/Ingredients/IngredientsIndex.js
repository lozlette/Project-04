import React from 'react'
import 'bulma'
import axios from 'axios'
import IngredientsCard from './IngredientsCard'
// import { Link } from 'react-router-dom'
const choices = []
class IngredientsIndex extends React.Component {
  constructor() {
    super()

    this.state = {}
    this.handleClick = this.handleClick.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount(){
    axios.get('/api/ingredients')
      .then(res => this.setState({ ingredients: res.data }))
  }

  handleClick(e){
    choices.push(e.target.id)
    console.log(choices)
  }

  handleSubmit(){
    if (parseInt(choices[0]) === this.state.ingredients[0].id && parseInt(choices[1]) === this.state.ingredients[1].id)
      this.props.history.push('/recipes/1')
    else this.props.history.push('/ingredients')
    console.log(this.state.ingredients)
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
              <button onClick={this.handleClick}><IngredientsCard {...ingredient}/></button>
            </div>
          )}
        </div>
        <button className="button" onClick={this.handleSubmit}>Submit</button>
      </div>
    )
  }
}

export default IngredientsIndex
