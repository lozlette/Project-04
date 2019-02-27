import React from 'react'

const IngredientsCard = ({ name, image }) => {
  return (

    <div className="isImage">
      <figure className="image is-4by3">
        <img src={image} alt={name} />
        <div className="middle">
          <div className="text">{name}</div>
        </div>
      </figure>
    </div>
  )
}

export default IngredientsCard
