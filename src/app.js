import React from 'react'
import ReactDOM from 'react-dom'
import Home from './components/common/Home'
import IngredientsIndex from './components/Ingredients/IngredientsIndex'
import IngredientsShow from './components/Ingredients/IngredientsShow'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Register from './components/auth/Register'
import Login from './components/auth/Login'
import 'bulma'
import './style.scss'

class App extends React.Component{
  constructor(){
    super()
  }

  render(){
    return(
      <div>
        <BrowserRouter>
          <main>
            <Switch>
              <Route path="/ingredients/:id" component={IngredientsShow} />
              <Route path="/ingredients" component={IngredientsIndex} />
              <Route path="/register" component={Register} />
              <Route path="/login" component={Login} />
              <Route path="/" component={Home} />
            </Switch>
          </main>
        </BrowserRouter>
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
