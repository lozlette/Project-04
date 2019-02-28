import React from 'react'
import 'bulma'

class Home extends React.Component {
  constructor() {
    super()

  }


  render(){
    return(
      <div>
        <section className="hero is-success is-small">
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
        </section>
        <section>

        </section>
      </div>
    )
  }
}

export default Home
