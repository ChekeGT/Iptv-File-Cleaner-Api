"""Configuration related to PayPal payment processes."""

# PayPal
from paypalcheckoutsdk.core import (
    PayPalHttpClient,
    SandboxEnvironment,
    LiveEnvironment
)

# Django
from django.conf import settings

# Utilities
import sys


class PayPalClient:
    def __init__(self):
        self.client_id = settings.PAYPAL_CLIENT_ID
        self.client_secret = settings.PAYPAL_CLIENT_SECRET

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use ProductionEnvironment."""
        
        payment_environment = self.get_environment()

        self.environment = payment_environment(client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key, value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                self.object_to_json(value) if not self.is_primittive(value) else value
        return result

    def array_to_json_array(self, json_array):
        result = []
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, int)

    @staticmethod
    def get_environment():
        """Returns environment based if project is being used on production or not"""

        return SandboxEnvironment if settings.DEBUG else LiveEnvironment
