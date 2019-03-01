import React from 'react'
import 'bulma'
import axios from 'axios'
import Auth from '../../lib/Auth'
// import CommentsForm from '/CommentsForm'


class RecipesShow extends React.Component {
  constructor() {
    super()

    this.state = {

    }

  }

  componentDidMount(){
    axios.get(`/api/recipes/${this.props.match.params.id}`,
      {headers: { Authorization: `Bearer ${Auth.getToken()}` }} )
      .then(res => this.setState({ recipes: res.data }))
  }

  render(){
    console.log(this.state)
    if(!this.state.recipes) return <h1>Loading...</h1>
    console.log(this.state.recipes)
    const { image, name, extra_ingredients } = this.state.recipes
    return(
      <div className="tile maintile is-ancestor">
        <div className="tile is-vertical is-12">
          <div className="tile">
            <div className="tile is-parent is-vertical">
              <article className="tile is-child box notification is-white">
                <figure className="image is-4by3 Middle">
                  <img src={image} alt={name} />
                </figure>
              </article>
              <article className="tile is-child box notification is-success">
                <p className="title is-success">Nutrition of ingredient 1</p>
              </article>
            </div>
            <div className="tile is-parent box">
              <article className="tile is-child notification is-success">
                <h2 className="title is-2">Ingredients</h2>
                <p className="subtitle is-4">{extra_ingredients}</p>

              </article>
            </div>
            <div className="tile is-parent box">
              <article className="tile is-child notification is-white">
                <h2 className="title is-2">Comments</h2>
                <p className="subtitle is-4">comments go here...</p>

              </article>
            </div>
          </div>
          <div className="tile is-parent">
            <article className="tile is-child notification is-success">
              <div className="content">
              </div>
            </article>
          </div>
        </div>
      </div>
    )
  }
}

export default RecipesShow
