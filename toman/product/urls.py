from django.urls import path
from transaction.views import OrderProductView
from product import views

urlpatterns = [
    path('create_product', views.CreateProductView.as_view(), name='create product'),
    path('product_list', views.ProductDetailsView.as_view(), name='product list'),
    path('order_product', OrderProductView.as_view(), name='payment product'),
]
