import React from 'react'
import 'bulma'
import axios from 'axios'
import Auth from '../../lib/Auth'
import MessagesForm from './MessagesForm'


class UserShow extends React.Component {
  constructor() {
    super()

    this.state = {
      messageText: ''
    }

  }

  getUser(){
    axios.get(`/api/users/${this.props.match.params.id}`)
      .then(res => this.setState({ user: res.data }))
  }

  componentDidMount(){
    this.getUser()
  }

  handleChangeMessage(e) {
    const text = e.target.value
    this.setState({
      messageText: { text }
    })
  }

  handleSubmitComment(e){
    e.preventDefault()
    console.log('HandleSubmit',this.state.messaageText)

    const messageText = {...this.state.messageText, user: this.state.user}
    axios
      .post('/api/users', messageText,
        { headers: { Authorization: `Bearer ${Auth.getToken()}` }}
      )
      .then(res => {
        console.log('res', res)
        this.setState({
          messageText: ''
        })
        this.getUser()
      })
      .catch(err => alert(err.message))
  }
  render() {
    if(!this.state.user) return <h1>Loading...</h1>
    console.log(this.state.user)
    const { username, email, avatar} = this.state.user
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
        <div className="container has-text-centered">
          <div className="column is-4 is-offset-4">
            <h3 className="title is-3">Swap recipe tips with your friends..</h3>
            <MessagesForm />
          </div>

        </div>

      </div>
    )
  }
}
export default UserShow
