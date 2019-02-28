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
    const { username, email, avatar } = this.state.users
    return (

      <div>
        <div className="card">
          <hr/>
          <div className="card-header">
            <h1 className="card-header-title">{username}</h1>
          </div>

          <div className="card-image">
            <figure className="image is-128x128">
              <img className="is-rounded" src={avatar} alt={username}/>
            </figure>
          </div>
        </div>

        <div className="card-content">
          <div className="content">
            <p><strong>Email:</strong>{email}</p>
          </div>
        </div>
      </div>
    )
  }
}
export default UserShow
