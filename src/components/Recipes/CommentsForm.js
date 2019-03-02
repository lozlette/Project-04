import React from 'react'

const CommentsForm = ({ handleChangeComment, handleSubmitComment, commentData }) => {
  return(
    <form onSubmit={handleSubmitComment}>
      <div className="field">
        <div className="control">
          <textarea
            className="textarea"
            name="content"
            placeholder="Please give feedback on this recipe!"
            defaultValue={commentData.content}
            onChange={handleChangeComment}
            maxLength="250"
            rows="6">
          </textarea>
        </div>
      </div>
      <button className="button is-white is-fullwidth"> Add Comment </button>
    </form>
  )
}
export default CommentsForm
