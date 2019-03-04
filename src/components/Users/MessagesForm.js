import React from 'react'

const MessagesForm = ({ handleChange, handleSubmit, data }) => {
  console.log(data)
  return(
    <form onSubmit={handleSubmit}>
      <div className="field">
        <div className="control">
          <input
            className="input"
            name="receiver_id"
            type="text"
            value={data.receiver_id}
            onChange={handleChange}
            placeholder="To: (enter username here)"></input>
        </div>
      </div>
      <div className="field">
        <div className="control">
          <textarea
            className="textarea"
            name="content"
            placeholder="Enter your message here"
            value={data.content}
            onChange={handleChange}
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
