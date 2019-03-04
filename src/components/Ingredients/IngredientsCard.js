import React from 'react'

const IngredientsCard = ({ name, image, id }) => {
  return (

    <div
      className="image"
      style={{ backgroundImage: `url(${image})` }}
      id={id}>
      <span>{name}</span>
    </div>
  )
}

export default IngredientsCard
