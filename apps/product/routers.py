from rest_framework import routers

from apps.product.views import ProductViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'products', ProductViewSet, basename='products')
