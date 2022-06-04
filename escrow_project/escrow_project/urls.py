from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_yasg import openapi

from rest_framework import routers
from rest_framework.schemas import get_schema_view as schema
from drf_yasg.views import get_schema_view

from products.urls import router as products_router


router = routers.DefaultRouter()
router.registry.extend(products_router.registry)


schema_view = get_schema_view(
    openapi.Info(
        title="Escrow Products API Document",
        default_version='v1',
        description="Test description",
    ),
    public=True,
)


urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=True)),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/auth-token/', include('dj_rest_auth.urls')),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/openapi/', schema(
        title='Escrow product endpoint for TomanPay',
        description='This API is for testing skills!'),
        name='openapi-shema'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
