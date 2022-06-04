from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.request import is_form_media_type

schema_view = get_schema_view(
   openapi.Info(
      title="excrow APIS",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
