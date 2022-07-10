from rest_framework import routers
from apps.user.routers import router_v1 as user_router_v1
from apps.file.routers import router_v1 as file_router_v1
from apps.product.routers import router_v1 as product_router_v1

app_router_v1 = routers.DefaultRouter()
app_router_v1.registry.extend(user_router_v1.registry)
app_router_v1.registry.extend(file_router_v1.registry)
app_router_v1.registry.extend(product_router_v1.registry)
