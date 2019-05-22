"""Payment processes related views."""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from IptvFileCleaner.users.serializers import UserModelSerializer
from IptvFileCleaner.payments.serializers import BuyAppByPaypalSerializer

# Status
from rest_framework.status import (
    HTTP_200_OK
)


class TransactionCompleteAPIView(APIView):
    """Manages verifying the transaction and making the user premium"""

    def post(self, request, *args, **kwargs):
        """Verifies the transaction and makes the user premium"""

        serializer = BuyAppByPaypalSerializer(
            data=request.data,
            context={
                'request': self.request,
                'format': self.format_kwarg,
                'view': self
            }
        )

        if serializer.is_valid(raise_exception=True):

            user = serializer.save()

            data = {
                'user': UserModelSerializer(user).data
            }
            return Response(data=data, status=HTTP_200_OK)
