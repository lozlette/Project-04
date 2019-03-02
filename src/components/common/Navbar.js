import React from 'react'
import { Link, withRouter } from 'react-router-dom'

import Auth from '../../lib/Auth'

class Navbar extends React.Component {

  constructor(props){
    super(props)

    this.state = {
      navbarOpen: false
    }

    this.toggleNavbar = this.toggleNavbar.bind(this)
    this.logout = this.logout.bind(this)
  }


  toggleNavbar() {
    this.setState({ navbarOpen: !this.state.navbarOpen })
  }




  logout(){
    Auth.removeToken()
    this.props.history.push('/')
  }

  componentDidUpdate(prevprops){
    if(prevprops.location.pathname !== this.props.location.pathname){
      this.setState({ navbarOpen: false})
    }
  }

  render() {
    return (
      <nav className="navbar is-success">
        <div className="container">
          <div className="navbar-brand">
            <Link className="navbar-item" to="/">
              Home
            </Link>
            <a className={`navbar-burger ${this.state.navbarOpen ? 'is-active' :'' }`}
              onClick={this.toggleNavbar}>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>
          <div className="navbar-menu">
            <div className="navbar-end">
              {Auth.isAuthenticated() && <Link className="navbar-item" to="/ingredients">Choose your ingredients</Link>}
              {Auth.isAuthenticated() && <Link className="navbar-item" to="/users/:id">Profile page</Link>}
              {!Auth.isAuthenticated() && <Link className="navbar-item" to="/register">Register</Link>}
              {!Auth.isAuthenticated() &&<Link className="navbar-item" to="/login">Login</Link>}
              {Auth.isAuthenticated() && <a className="navbar-item" onClick={this.logout}>Logout</a>}
            </div>
          </div>
        </div>
      </nav>
    )
  }
}

export default withRouter(Navbar)
