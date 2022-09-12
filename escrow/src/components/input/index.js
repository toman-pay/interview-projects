import React from "react"

import { clsx } from "clsx"

import "./index.scss"

const Input = ({
  onChange,
  onBlur,
  value,
  placeholder,
  type,
  label,
  name,
  error,
  isTextArea = false,
  inputSuffix = null,
}) => {
  return (
    <div className="component-input">
      <label htmlFor={name}>{label}</label>
      <div className={clsx("field-wrapper", error && "has-error")}>
        {isTextArea ? (
          <textarea
            className="field"
            id={name}
            onChange={onChange}
            onBlur={onBlur}
            value={value}
            placeholder={placeholder}
            type={type}
            rows={4}
          />
        ) : (
          <div className="row">
            <input
              className="field"
              id={name}
              onChange={onChange}
              onBlur={onBlur}
              value={value}
              placeholder={placeholder}
              type={type}
            />
            <>{inputSuffix}</>
          </div>
        )}
      </div>

      {error && <span className="error">{error}</span>}
    </div>
  )
}

export default Input
