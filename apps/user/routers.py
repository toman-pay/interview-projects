from rest_framework import routers

from apps.user.views import UserDetailView

router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UserDetailView, basename='users')
