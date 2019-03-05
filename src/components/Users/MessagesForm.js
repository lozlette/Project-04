import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class MessagesForm extends React.Component {
  constructor(props) {
    super(props)

    this.state = {}

  }

  componentDidMount(){
    axios.get('/api/users', { headers: { Authorization: `Bearer ${Auth.getToken()}` }})
      .then(res => this.setState({ users: res.data }))
  }




  render(){
    if(!this.state.users) return <h1>Loading...</h1>
    const { handleChange, handleSubmit, data } = this.props
    console.log('data', data)
    return(
      <form onSubmit={handleSubmit}>
        <div className="field">
          <div className="control has-icons-left">
            <div className="select is-fullwidth">
              <select name="receiver_id" onChange={handleChange}>
                <option>To:</option>
                {this.state.users.map(user =>
                  <option key={user.id} value={user.id}>{user.username}</option>
                )}
              </select>
              <div className="icon is-small is-left">
                <i className="fas fa-envelope"></i>
              </div>
            </div>
          </div>
        </div>
        <div className="field">
          <div className="control">
            <textarea
              className="textarea"
              name="content"
              placeholder="Enter your message here"
              value={data.content}
              onChange={handleChange}
              maxLength="250"
              rows="6">
            </textarea>
          </div>
        </div>
        <button className="button is-white is-fullwidth"> SEND </button>
      </form>
    )
  }
}
export default MessagesForm
