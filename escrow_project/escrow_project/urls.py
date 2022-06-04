from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from rest_framework import routers

from products.urls import router as products_router


router = routers.DefaultRouter()
router.registry.extend(products_router.registry)


urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=True)),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)