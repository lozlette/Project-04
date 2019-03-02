import React from 'react'
import 'bulma'
import axios from 'axios'
import Auth from '../../lib/Auth'
import CommentsForm from './CommentsForm'


class RecipesShow extends React.Component {
  constructor() {
    super()

    this.state = {
      commentData: {
        content: ''
      }

    }

    this.handleChangeComment = this.handleChangeComment.bind(this)
    this.handleSubmitComment = this.handleSubmitComment.bind(this)
    this.getRecipe = this.getRecipe.bind(this)

  }

  getRecipe(){
    axios.get(`/api/recipes/${this.props.match.params.id}`,
      {headers: { Authorization: `Bearer ${Auth.getToken()}` }} )
      .then(res => this.setState({ recipe: res.data }))
  }

  componentDidMount(){
    this.getRecipe()
    // axios.get(`/api/recipes/${this.props.match.params.id}`,
    //   {headers: { Authorization: `Bearer ${Auth.getToken()}` }} )
    //   .then(res => this.setState({ recipe: res.data }))
  }

  handleChangeComment({ target: {name, value }}) {
    // console.log(name)
    const commentData = {...this.state.commentData, [name]: value }
    this.setState({ commentData })
  }

  handleSubmitComment(e){
    e.preventDefault()
    console.log('HandleSubmit',this.state.commentData)

    const commentData = {...this.state.commentData, recipe: this.state.recipe}
    axios
      .post(`/api/recipes/${this.props.match.params.id}/comments`, commentData,
        { headers: { Authorization: `Bearer ${Auth.getToken()}` }}
      )
      .then(res => {
        console.log('res', res)
        this.setState({
          commentData: {
            content: ''
          }
        })
        this.getRecipe()
      })
      .catch(err => alert(err.message))
  }

  render(){
    // console.log(this.state)
    if(!this.state.recipe) return <h1>Loading...</h1>
    console.log(this.state.recipe)
    const {
      image,
      name,
      extra_ingredients: extraIngredients,
      comments,
      ingredients,
      method
    } = this.state.recipe
    console.log('RECIPE SHOW STATE',this.state)
    return(

      <div>
        <section className="hero is-success is-small">
          <div className="hero-body">
            <div className="container">
              <h1 className="title">
                {name}
              </h1>

            </div>
          </div>
        </section>
        <div className="tile maintile is-ancestor">
          <div className="tile is-vertical is-12">
            <div className="tile">
              <div className="tile is-parent is-vertical">
                <article className="tile is-child box notification is-white">
                  <figure className="image is-4by3">
                    <img src={image} alt={name} />
                  </figure>
                </article>
                <article className="tile is-child box notification is-success">
                  {ingredients.map(ingredient =>
                    <div key={ingredient.id}>
                      <h2 className="title is-2 is-white">Nutrition information on {ingredient.name}</h2>
                      <p>{ingredient.nutrition_information}</p>
                      <hr/>
                    </div>
                  )}
                </article>
              </div>
              <div className="tile is-parent box">
                <article className="tile is-child notification is-success">
                  <h2 className="title is-2">Ingredients</h2>
                  <p className="subtitle is-4">{extraIngredients}</p>
                  <hr/>
                  <h2 className="title is-2">Method</h2>
                  <p className="subtitle is-4">{method}</p>

                </article>
              </div>
              <div className="tile is-parent box">
                <article className="tile is-child notification is-success">
                  <h2 className="title is-2">Comments</h2>

                  {this.state.commentData &&
                    <CommentsForm
                      handleChangeComment={this.handleChangeComment}
                      handleSubmitComment={this.handleSubmitComment}
                      commentData={this.state.commentData}
                    />
                  }

                </article>
              </div>
            </div>
            <div className="tile is-parent">
              <article className="tile is-child notification is-success">
                <div className="content">
                  <h2 className="title is-2">See feedback on this recipe</h2>
                  {comments.map(comment =>
                    <div key={comment.id}>
                      <h3 className="title is-4 is-white">{comment.user.username} says:</h3>
                      <p>{comment.content}</p>
                      <p>{comment.user.created_at}</p>
                      <hr/>
                    </div>
                  )}
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default RecipesShow
