"""Link model declaration."""

# Django
from django.db import models

# Models
from .payment import Payment


class Link(models.Model):
    """Link model."""

    rel = models.CharField(max_length=50)
    href = models.URLField()
    method = models.CharField(max_length=15)
    payment = models.ForeignKey(Payment, related_name='links', on_delete=models.CASCADE)
