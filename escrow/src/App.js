import React, { useState } from "react"

import { Form, Formik } from "formik"
import { ToastContainer, toast } from "react-toastify"

import "react-toastify/dist/ReactToastify.css"
import "./App.scss"

import api from "src/api"

import Input from "src/components/input"
import Header from "src/components/header"
import Button from "src/components/button"
import CheckBox from "src/components/checkbox"
import EulaDrawer from "src/components/EulaDrawer"

import { FormSchema } from "src/helpers/validation/schema"

import ProductLogo from "src/assets/images/product.svg"

const initialValues = {
  title: "",
  price: "",
  description: "",
}

function App() {
  const [showEula, setShowEula] = useState(false)
  const [hasAccepted, setHasAccepted] = useState(false)
  const [isSubmitting, setIsSubmitting] = useState(false)

  const openEulaModal = () => {
    setShowEula(true)
  }

  const onAccept = () => {
    setShowEula(false)
    setHasAccepted(true)
  }

  const onSubmit = (values) => {
    if (isSubmitting) {
      return
    }
    setIsSubmitting(true)
    api.form
      .submit({
        title: values.title,
        price_tomans: +values.price,
        description: values.description,
      })
      .then(() => {
        toast.success("با موفقیت ثبت شد.")
      })
      .catch((err) => {
        console.log(err)
        toast.error("خطایی رخ داده است.")
      })
      .finally(() => setIsSubmitting(false))
  }

  return (
    <>
      <div className="app">
        <Header title="ساخت تراکنش" />

        <div className="form-title">
          <img src={ProductLogo} className="icon" alt="product-icon" />
          <div className="title">اطلاعات محصول</div>
        </div>

        <Formik
          initialValues={initialValues}
          validationSchema={FormSchema}
          onSubmit={onSubmit}
        >
          {({ errors, touched, handleChange, handleBlur, submitForm }) => (
            <Form className="main-form">
              <div>
                <Input
                  label="عنوان محصول"
                  name="title"
                  error={touched.title && errors.title}
                  onChange={handleChange("title")}
                  onBlur={handleBlur("title")}
                />

                <Input
                  label="قیمت"
                  name="price"
                  inputSuffix={<div className="toman-sufix">تومان</div>}
                  error={touched.price && errors.price}
                  onChange={handleChange("price")}
                  onBlur={handleBlur("price")}
                />

                <Input
                  label="توضیحات"
                  name="description"
                  isTextArea
                  error={touched.description && errors.description}
                  onChange={handleChange("description")}
                  onBlur={handleBlur("description")}
                />

                <CheckBox
                  checked={hasAccepted}
                  onChange={(e) => setHasAccepted(e.target.checked)}
                  label={
                    <>
                      <span className="primary-text" onClick={openEulaModal}>
                        شرایط و قوانین
                      </span>
                      <span> را می‌پذیریم.</span>
                    </>
                  }
                />
              </div>
              <div className="button-wrapper">
                <Button
                  type="submit"
                  disabled={!hasAccepted}
                  onClick={submitForm}
                >
                  {isSubmitting ? "لطفا منتظر بمانید" : "تایید"}
                </Button>
              </div>
            </Form>
          )}
        </Formik>

        <EulaDrawer
          isOpen={showEula}
          setIsOpen={setShowEula}
          onAccept={onAccept}
        />
        <ToastContainer position="top-center" rtl />
      </div>
    </>
  )
}

export default App
