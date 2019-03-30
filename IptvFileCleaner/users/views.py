"""Users app views module."""

# Django REST Framework
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import  Response

# Serializers
from .serializers import UserModelSerializer, UserSignupSerializer

# Status
from rest_framework.status import (
    HTTP_201_CREATED
)


class UserManagementViewSet(ViewSet):
    """Manages all the views related with the managament of an user."""

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Handles the signup of an user."""
        data = request.data
        serializer = UserSignupSerializer(data=data)

        if serializer.is_valid(raise_exception=True):

            user = serializer.save()

            data = {
                'user': UserModelSerializer(user).data
            }
            import ipdb; ipdb.set_trace()
            return Response(data=data, status=HTTP_201_CREATED)