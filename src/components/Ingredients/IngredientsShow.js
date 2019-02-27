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
    const { image, name } = this.state.ingredients
    return(
      <div>
        <div className="columns">
          <div className="column is-one-half">
            <div className="column">
              <figure className="image is-4by2">
                <img src={image} alt={name} />
              </figure>
            </div>
          </div>
          <div className="column is-one-half">
          </div>
        </div>
      </div>
    )
  }
}

export default IngredientsShow
