import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Register extends React.Component{
  constructor (){
    super()

    this.state = {
      data: {
        username: '',
        email: '',
        password: '',
        password_confirmation: '',
        avatar: ''
      }
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({target: {name, value}}){
    const data ={ ...this.state.data, [name]: value}
    this.setState({data})
  }


  handleSubmit(e) {
    e.preventDefault()
    axios
      .post('/api/register', this.state.data)
      .then( res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/login')
      })
      .catch(err => this.setState({ errors: err.response.data.error }))
      .then(() => console.log(this.state))
  }
  render(){
    const{username,email, password, password_confirmation, avatar} = this.state.data

    return(
      <main className= "section">
        <div className="container">
          <form onSubmit= {this.handleSubmit}>
            <h2 className="title"> Register </h2>

            <div className="field">
              <label className="label"> Username</label>
              <input
                name="username"
                placeholder="Username"
                value={username}
                onChange={this.handleChange}
              />
            </div>

            <div className="field">
              <label className="label"> Email </label>
              <input
                name="email"
                placeholder="Email"
                value={email}
                onChange={this.handleChange}
              />
            </div>

            <div className="field">
              <label className="label"> Password </label>
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={password}
                onChange={this.handleChange}
              />
            </div>

            <div className="field">
              <label className="label"> Password Confirmation </label>
              <input
                type="password"
                name="password_confirmation"
                placeholder="Password Confirmation"
                value={password_confirmation}
                onChange={this.handleChange}
              />
            </div>

            <div className="field">
              <label className="label"> Image </label>
              <input
                type="avatar"
                name="avatar"
                placeholder="Image"
                value={avatar}
                onChange={this.handleChange}
              />
            </div>

            <button className='button is-primary'>Submit</button>
          </form>
        </div>
      </main>
    )

  }
}

export default Register
