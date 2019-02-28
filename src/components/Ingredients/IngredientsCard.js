import React from 'react'

const IngredientsCard = ({ name, image, id }) => {
  return (

    <div className="isImage">
      <figure className="image">
        <img src={image} alt={name} id={id}/>
      </figure>
    </div>
  )
}

export default IngredientsCard
