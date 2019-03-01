import React from 'react'

const CommentsForm = ({ handleChangeComment, handleSubmitComment, commentData }) => {
  return(
    <form onSubmit={handleSubmitComment}>
      <textarea
        className="textarea"
        name="content"
        placeholder="Add your comments!"
        defaultValue={commentData.content}
        onChange={handleChangeComment}
        maxLength="250"
        rows="6">
      </textarea>
      <button className="button is-success"> Add Commment </button>
      <p>{commentData.content}</p>
    </form>
  )
}
export default CommentsForm
