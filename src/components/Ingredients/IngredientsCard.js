import React from 'react'

const IngredientsCard = ({ name, image }) => {
  return (

    <div className="isImage">
      <figure className="image">
        <img src={image} alt={name} />
      </figure>
    </div>
  )
}

export default IngredientsCard
