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
      <section className= "hero has-background-primary">
        <div className="hero-body">
          <div className="column is-4 is-offset-4">
            <h4 className="title has-text-centered">Register</h4>
            <div className="box">
              <form onSubmit= {this.handleSubmit}>
                <div className="field">
                  <div className="control">
                  </div>
                  <div className="field">
                    <label className="label is-large"> Username</label>
                    <div className="controls">
                      <input
                        className="input"
                        name="username"
                        placeholder="Username"
                        value={username}
                        onChange={this.handleChange}
                      />
                    </div>
                  </div>
                  <div className="field">
                    <label className="label is-large"> Email </label>
                    <div className="control">
                      <input
                        type="email"
                        className="input"
                        name="email"
                        placeholder="Email"
                        value={email}
                        onChange={this.handleChange}
                      />
                    </div>
                  </div>
                  <div className="field">
                    <label className="label is-large"> Password </label>
                    <div className="control">
                      <input
                        className="input"
                        type="password"
                        name="password"
                        placeholder="Password"
                        value={password}
                        onChange={this.handleChange}
                      />
                    </div>
                  </div>
                  <div className="field">
                    <label className="label is-large"> Password Confirmation </label>
                    <div className="control">
                      <input
                        className="input"
                        type="password"
                        name="password_confirmation"
                        placeholder="Password Confirmation"
                        value={password_confirmation}
                        onChange={this.handleChange}
                      />
                    </div>
                  </div>

                  <div className="field">
                    <label className="label is-large"> Image </label>
                    <div className="control">
                      <input
                        className="input"
                        type="avatar"
                        name="avatar"
                        placeholder="Image"
                        value={avatar}
                        onChange={this.handleChange}
                      />
                    </div>
                  </div>
                </div>
                <button className="button is-success is-medium is-fullwidth">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default Register
