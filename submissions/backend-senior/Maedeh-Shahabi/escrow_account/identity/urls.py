from django.urls import path
from rest_framework.routers import DefaultRouter

from identity.views.create_user_view import CreateUserView

app_name = "identity"

router = DefaultRouter()

urlpatterns = [

    path('user/create/', CreateUserView.as_view(), name="create_user_view"),

]

urlpatterns += router.urls
