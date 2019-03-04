// allows us to write our tests in ES6
require('@babel/register')()

// setup JSDOM (javascript DOM)
const { JSDOM } = require('jsdom')
//fake window
const { window } = new JSDOM(`
  <!DOCTYPE html>
  <html>
  <body></body>
  </html>
`, {
  url: 'http://localhost'
})

window.localStorage = (function() {
  const store = {}

  return {
    getItem(key) {
      return store[key]
    },
    setItem(key, value) {
      store[key] = value
    },
    removeItem(key) {
      delete store[key]
    }
  }
})

// setup Enzyme (Enzyme is a way to test React)
const Adapter = require('enzyme-adapter-react-16')
require('enzyme').configure({ adapter: new Adapter() })

// copy any global properties from `window` to `global`
const props = Object.getOwnPropertyNames(window)
  .filter(prop => typeof global[prop] === 'undefined')
  .map(prop => Object.getOwnPropertyDescriptor(window, prop))

Object.defineProperties(global, props)

global.window = window
global.localStorage = window.localStorage
global.document = window.document
