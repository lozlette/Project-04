import React from 'react'
import 'bulma'
import axios from 'axios'


class UserShow extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get(`/api/users/${this.props.match.params.id}`)
      .then(res => this.setState({ users: res.data }))
  }
  render() {
    if(!this.state.users) return <h1>Loading...</h1>
    console.log(this.state.users)
    const { username, email, avatar} = this.state.users
    return (
      <div>
        <section className="hero is-success is-small">
          <div className="hero-body">
            <div className="container">
              <h1 className="title has-text-centered">
                {username}:
              </h1>
            </div>
          </div>
        </section>
        <div className="container has-content-centered">
          <div className="column user-page">
            <div className="card-image is-centered">
              <figure className="image is-200x200">
                <img className="is-rounded" src={avatar} alt={username}/>
              </figure>
            </div>
          </div>
        </div>

        <div className="container has-text-centered">
          <div className="column is-4 is-offset-4">
            <div className="card-content is-centered">
              <div className="content">
                <p className="user-p"><strong>Email:</strong>{email}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    )
  }
}
export default UserShow
