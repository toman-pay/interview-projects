from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import SubmitProductView

app_name = "products"

router = DefaultRouter()

urlpatterns = [

    path('submit/', SubmitProductView.as_view(), name="submit_product_view"),

]

urlpatterns += router.urls
