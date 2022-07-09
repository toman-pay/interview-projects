from rest_framework import routers
from apps.user.routers import router_v1 as user_router_v1


app_router_v1 = routers.DefaultRouter()
app_router_v1.registry.extend(user_router_v1.registry)
