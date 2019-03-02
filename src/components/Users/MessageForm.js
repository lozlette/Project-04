import React from 'react'

const MessagesForm = ({ handleChangeMessage, handleSubmitMessage, messageData }) => {
  return(
    <form onSubmit={handleSubmitMessage}>
      <div className="field">
        <div className="control">
          <textarea
            className="textarea"
            name="content"
            placeholder="Please give feedback on this recipe!"
            defaultValue={messageData.content}
            onChange={handleChangeMessage}
            maxLength="250"
            rows="6">
          </textarea>
        </div>
      </div>
      <button className="button is-white is-fullwidth"> Add Message </button>
    </form>
  )
}
export default MessagesForm
