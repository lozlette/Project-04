class Auth{
  static setToken(token){
    localStorage.setItem('token', token)
  }

  static getToken(){
    return localStorage.getItem('token')
  }

  static removeToken(){
    localStorage.removeItem('token')
  }

  static getUserID(){
    return this.getPayload().sub
  }

  static getPayload (){
    const token = this.getToken()
    if(!token) return false
    const parts= token.split('.')
    if(parts.length<3) return false
    try {
      return JSON.parse(atob(parts[1]))
    } catch {
      return false
    }
  }
  static isAuthenticated(){
    const payload = this.getPayload()
    if(!payload) return false
    const now = Math.round(Date.now() /1000)
    return now < payload.exp
  }
}
export default Auth
