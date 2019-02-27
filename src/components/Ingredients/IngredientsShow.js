import React from 'react'
import 'bulma'
import axios from 'axios'


class IngredientsShow extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get(`/api/ingredients/${this.props.match.params.id}`)
      .then(res => this.setState({ ingredients: res.data }))
  }

  render(){
    if(!this.state.ingredients) return <h1>Loading...</h1>
    console.log(this.state.ingredients)
    const { image, name, nutrition_information } = this.state.ingredients
    return(
      <div className="tile is-ancestor">
        <div className="tile is-vertical is-8">
          <div className="tile">
            <div className="tile is-parent is-vertical">
              <article className="tile is-child box notification is-white">
                <figure className="image is-4by3">
                  <img src={image} alt={name} />
                </figure>
              </article>
              <article className="tile is-child box notification is-success">
                <p className="title is-success">Nutrition of a {name}</p>
                <p className="subtitle">{nutrition_information}</p>
              </article>
            </div>
            <div className="tile is-parent box">
              <article className="tile is-child notification is-white">

              </article>
            </div>
          </div>
          <div className="tile is-parent">
            <article className="tile is-child notification is-success">
              <p className="title">Comments</p>
              <p className="subtitle">comments go here..</p>
              <div className="content">
              </div>
            </article>
          </div>
        </div>
      </div>
    )
  }
}

export default IngredientsShow
