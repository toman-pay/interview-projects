from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from apps.user.serializers import UserSerializer

User = get_user_model()


class UserDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, url_path='whoami', methods=["GET"])
    def whoami(self, request):
        serializer = UserSerializer(request.user, many=False)
        return Response(data=serializer.data)
