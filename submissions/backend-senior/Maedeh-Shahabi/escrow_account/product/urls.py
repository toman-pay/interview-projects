from django.urls import path
from rest_framework.routers import DefaultRouter

from product.views.submit_product_view import SubmitProductView

app_name = "product"

router = DefaultRouter()

urlpatterns = [

    path('submit/', SubmitProductView.as_view(), name="submit_product_view"),

]

urlpatterns += router.urls
