import React from 'react'
import axios from 'axios'


class UserShow extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get('/api/users')
      .then(res => this.setState({ users: res.data }))
  }
  render() {
    if(!this.state.users) return <h1>Loading...</h1>
    console.log(this.state.users)
    return (
      <div className="isImage">
        <figure className="image is-4by3">
          <img src={this.state.users.avatar} alt={this.state.users.username} />
          <div className="middle">
            <div className="text">{this.state.users.username}</div>
          </div>
        </figure>
      </div>
    )
  }
}
export default UserShow
