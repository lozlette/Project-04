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
    console.log('HandleSubmit',this.state.content)

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
                {username}'s Profile Page
              </h1>
            </div>
          </div>
        </section>


        <div className="columns is-multiline">
          <div className="column usercolumn is-half has-background-primary">
            <div className="card-image is-centered">
              <figure className="image" id="userimage">
                <img className="is-square" src={avatar} alt={username}/>
              </figure>
            </div>
          </div>
          <div className="column usercolumn is-half has-background-primary">
            <div className="card-content is-centered">
              <div className="content">
                <h2 className="title is-2" id="h2">Details:</h2>
                <hr/>
                <p className="userp">Email: {email}</p>
              </div>
            </div>
          </div>
          <div className="column usercolumn is-half has-background-primary">
            <h2 className="title is-2" id="h2">Swap recipe tips with your friends..</h2>
            <MessagesForm
              handleChange={this.handleChange}
              handleSubmit={this.handleSubmit}
              data={this.state}
            />
          </div>
          <div className="column usercolumn is-half has-background-primary">
            <div className="card-content is-centered">
              <div className="content">
                <h2 className="title is-2" id="h2">Inbox:</h2>
                <hr/>
                <div>
                  {inbox.map(item =>
                    <div key={item.id}>
                      <p className="userp2 ">From: {item.sender.username}</p>
                      <p className="userp2">Message:</p>
                      <h3 id="userh3">{item.content}</h3>
                      <p className="userp2">On: {item.created_at}</p>
                      <hr/>
                    </div>)}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
export default UserShow
