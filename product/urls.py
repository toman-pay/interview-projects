from django.urls import path

from product import views

urlpatterns = [
    path("product/create/", views.CreateProductView.as_view(), name="product-create"),
    path(
        "product-image/create/", views.CreateProductImageView.as_view(), name="product-image-create"
    ),
]
