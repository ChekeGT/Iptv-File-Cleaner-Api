"""Utilities for using PayPal config."""


# PayPal
from .config import PayPalClient
from paypalcheckoutsdk.orders import OrdersGetRequest

# Models
from .models import Link, Payment


class GetOrder(PayPalClient):

    """You can use this function to retrieve an order by passing order ID as an argument"""
    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        
        response = self.client.execute(request)

        status_code = response.status_code
        status = response.result.status
        order_id = response.result.id
        intent = response.result.intent

        payment = Payment.objects.create(
            status_code=status_code,
            status=status,
            order_id=order_id,
            intent=intent,
        )

        for link in response.result.links:
            Link.objects.create(
                rel=link.rel,
                href=link.href,
                method=link.method,
                payment=payment
            )

        return status_code == 200
