import React from 'react'
import ReactDOM from 'react-dom'
import Home from './components/common/Home'
import Navbar from './components/common/Navbar'
import IngredientsIndex from './components/Ingredients/IngredientsIndex'
import RecipesShow from './components/Recipes/RecipesShow'
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

            <Navbar />
            <Switch>
              <Route path="/recipes/:id" component={RecipesShow} />
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
