"""Payments app urls."""

# Django
from django.urls import path

# Views
from .views import TransactionCompleteAPIView

urlpatterns = [
    path('paypal/transaction-complete', TransactionCompleteAPIView.as_view(), name='transaction_complete')
]
