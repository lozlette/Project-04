import React from 'react'

const MessagesForm = ({ handleChangeMessage, handleSubmitMessage, messageText }) => {
  return(
    <form onSubmit={handleSubmitMessage}>
      <div className="field">
        <div className="control">
          <input className="input" type="text" placeholder="To:"></input>
        </div>
      </div>
      <div className="field">
        <div className="control">
          <textarea
            className="textarea"
            name="content"
            placeholder="Enter your message here"
            defaultValue={messageText}
            onChange={handleChangeMessage}
            maxLength="250"
            rows="6">
          </textarea>
        </div>
      </div>
      <button className="button is-white is-fullwidth"> SEND </button>
    </form>
  )
}
export default MessagesForm
