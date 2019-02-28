import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class CommentsForm extends React.Component{
  constructor(props){
    super(props)

    this.state={
      message: 'Post Successfully Created',
      finished: false,
      commentData: {
        content: ''
      }
    }
  }

  handleChangeComment({ target: {name, value }}) {
    console.log(name)
    const commentData = {...this.state.commentData, [name]: value }
    this.setState({ commentData })
  }

  handleSubmitComment(e){
    e.preventDefault()
    axios
      .post(`/api/recipes/${this.props.recipe.id}/posts`, this.state.commentData,
        { headers: { Authorization: `Bearer ${Auth.getToken()}` }}
      )
      .then(res => {
        this.setState({
          commentData: {
            content: ''
          }
        })
      })
      .then(this.props.reload)
      .catch(err => alert(err.message))
  }



  render(){
    const {handleChangeComment, handleSubmitComment, commentData } = this.props
    return(
      <div className="field">
        <div className="control">
          <textarea className="textarea" placeholder="Please comment on this recipe" value={commentData.content} rows="10" onChange={handleChangeComment}></textarea>
        </div>
        <div className="control">
          <button className="button is-link" onSubmit={handleSubmitComment}>Submit</button>
        </div>
      </div>
    )
  }

}
export default CommentsForm
