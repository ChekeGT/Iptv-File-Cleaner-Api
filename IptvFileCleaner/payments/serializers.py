"""Payments related serializers."""

# Django REST Framework
from rest_framework import serializers

# Status
from rest_framework.status import (
    HTTP_402_PAYMENT_REQUIRED
)

# Payments
from IptvFileCleaner.payments.utils import GetOrder

# Exceptions
from rest_framework.exceptions import APIException


class PaymentRequiredException(APIException):
    """Exception raised when a required payment is not successfully done."""

    status_code = HTTP_402_PAYMENT_REQUIRED
    default_detail = "The payment is not valid, please try again or verify your payment data."
    default_code = "payment_fail"


class BuyAppByPaypalSerializer(serializers.Serializer):
    """Manages giving the premium status to an user if a payment is successful, and also checking it."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    orderID = serializers.CharField(max_length=10000)

    def validate_orderID(self, order_id):
        """Validates order id is correct and the payment was done successfully."""

        if not GetOrder().get_order(order_id):
            raise PaymentRequiredException

    def save(self, **kwargs):
        """Manages transforming the user into premium."""

        user = self.validated_data['user']
        user.is_premium = True
        user.save()

        return user
