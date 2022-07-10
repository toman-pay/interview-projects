from rest_framework import routers

from apps.file.views import FileViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'files', FileViewSet, basename='files')
