from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from product.router import product_router
from product import router

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += product_router.urls
