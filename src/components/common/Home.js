import React from 'react'
import 'bulma'
import { Link } from 'react-router-dom'

class Home extends React.Component {
  constructor() {
    super()

  }


  render(){
    return(
      <div>
        <section className="hero is-small is-success">
          <div className="hero-body">
            <div className="container">
              <h1 className="title">
                Eat Something
              </h1>
              <h2 className="subtitle">
                Find recipes based on what your toddler likes to eat... and what you'd like your toddler to eat..
              </h2>
            </div>
          </div>
          <div className="imagecontainer">
          </div>
          <Link to={'/ingredients'}>
            <button className="button homebtn is-fullwidth is-success">Choose your Ingredients</button>
          </Link>
        </section>
      </div>
    )
  }
}

export default Home
