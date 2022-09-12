import React from "react"
import "./index.scss"

const CheckBox = ({ label, checked, onChange }) => {
  return (
    <div className="component-checkbox">
      <input type="checkbox" checked={checked} onChange={onChange} />
      <label>{label}</label>
    </div>
  )
}

export default CheckBox
