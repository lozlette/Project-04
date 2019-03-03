import React from 'react'
import axios from 'axios'

import Auth from '../../lib/Auth'

class Login extends React.Component{
  constructor(){
    super()

    this.state = {
      data: {
        email: '',
        password: ''
      }
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }
  handleChange({target: {name, value}}){
    const data = {...this.state.data, [name]: value}
    this.setState({data})
  }

  handleSubmit(e) {
    e.preventDefault()
    axios
      .post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/')
      })
      .catch(() => this.setState({errors: 'Invalid credentials'}))
  }


  render(){
    const{email, password} = this.state.data

    return(
      <section className= "hero has-background-primary ">
        <div className="hero-body">
          <div className="column is-4 is-offset-4">
            <h4 className="title has-text-centered">Login</h4>
            <div className="box">
              <form onSubmit={this.handleSubmit}>
                <div className="field">
                  <div className="control">
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
                </div>
                <button className="button is-success is-medium is-fullwidth"> Log in</button>
              </form>
            </div>
          </div>
        </div>
      </section>

    )
  }
}
export default Login
