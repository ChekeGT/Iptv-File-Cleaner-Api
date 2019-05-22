"""Payment model declaration."""

# Django
from django.db import models


class Payment(models.Model):
    """Payment model."""

    status_code = models.IntegerField()
    status = models.CharField(max_length=150)
    order_id = models.CharField(max_length=500)
    intent = models.CharField(max_length=150)
    amount = models.CharField(max_length=50)
