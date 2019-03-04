import React from 'react'
import 'bulma'
import axios from 'axios'
import Auth from '../../lib/Auth'
import MessagesForm from './MessagesForm'


class UserShow extends React.Component {
  constructor() {
    super()

    this.state = {
      content: '',
      receiver_id: ''
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.getUser = this.getUser.bind(this)
  }

  getUser(){
    axios.get(`/api/users/${this.props.match.params.id}`)
      .then(res => this.setState({ user: res.data }))
  }

  componentDidMount(){
    this.getUser()
  }

  handleChange(e) {
    this.setState({ [e.target.name]: e.target.value })
  }

  handleSubmit(e){
    e.preventDefault()
    console.log('HandleSubmit',this.state.messageText)

    axios
      .post(`/api/users/${this.state.receiver_id}/inbox`, this.state,
        { headers: { Authorization: `Bearer ${Auth.getToken()}` }}
      )
      .then(() => {
        this.setState({ content: '', receiver_id: '' })
      })
      .catch(err => alert(err.message))
  }
  render() {
    if(!this.state.user) return <h1>Loading...</h1>
    const { username, email, avatar, inbox} = this.state.user
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
        <div className="container has-background-primary has-content-centered">
          <div className="column user-page">
            <div className="card-image is-centered">
              <figure className="image is-200x200">
                <img className="is-rounded" src={avatar} alt={username}/>
              </figure>
            </div>
          </div>
        </div>
        <div className="container has-background-primary has-text-centered">
          <div className="column">
            <div className="card-content is-centered">
              <div className="content">
                <h2 className="title is-2 usertitle">Details:</h2>
                <p>Email: {email}</p>
              </div>
            </div>
          </div>
        </div>
        <div className="container has-background-primary has-text-centered">
          <div className="column is-4 is-offset-4">
            <h2 className="title usertitle is-2">Swap recipe tips with your friends..</h2>
            <MessagesForm
              handleChange={this.handleChange}
              handleSubmit={this.handleSubmit}
              data={this.state}
            />
          </div>
        </div>
        <div className="container has-background-primary has-text-centered">
          <div className="column is-4 is-offset-4">
            <div className="card-content is-centered">
              <div className="content">
                <h2 className="title usertitle is-2">Inbox:</h2>
                {inbox.map(item => <p key={username}>{item}</p>)}
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
export default UserShow
