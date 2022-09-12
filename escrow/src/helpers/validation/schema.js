import * as yup from "yup"

const title = yup
  .string()
  .min(3, "خیلی کوتاهه")
  .max(30, "خیلی بلنده")
  .required("یادت رفت بنویسی")

const description = yup
  .string()
  .max(150, "خیلی بلنده")
  .required("یادت رفت بنویسی")

const price = yup
  .number()
  .typeError("باید عدد وارد کنی")
  .min(0, "کمتر از صفر نباید باشه")
  .required("یادت رفت بنویسی")

export const FormSchema = yup.object().shape({
  title,
  price,
  description,
})
