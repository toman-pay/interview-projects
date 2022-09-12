import api from "./api.service"
import { productRoute } from "./routes"

const form = {
  submit: (data) => api.post(productRoute, data),
}

export default { form }
