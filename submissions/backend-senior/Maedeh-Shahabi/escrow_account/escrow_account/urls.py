"""escrow_account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
                  # Authentication URLs
                  path('api/v1/escrow_account/jwt/create/', TokenObtainPairView.as_view(), name='jwt_token_create'),
                  path('api/v1/escrow_account/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_token_refresh'),

                  # Product application URLs
                  path('api/v1/escrow_account/products/', include('product.urls', namespace='v1_products')),

                  # Identity application URLs
                  path('api/v1/escrow_account/identity/', include('identity.urls', namespace='v1_identity')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
