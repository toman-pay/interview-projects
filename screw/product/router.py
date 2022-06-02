from rest_framework import routers
from product.v1.api import ProductView


product_router = routers.DefaultRouter()

# API v1
product_router.register('v1/product', ProductView, basename='product')
