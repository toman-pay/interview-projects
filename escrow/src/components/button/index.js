import React from "react"
import { clsx } from "clsx"
import "./index.scss"

const Button = ({
  children,
  onClick = () => {},
  disabled = false,
  type = "",
}) => {
  return (
    <button
      className={clsx("component-button", disabled && "disabled")}
      onClick={onClick}
      type={type}
      disabled={disabled}
    >
      <div>{children}</div>
    </button>
  )
}

export default Button
