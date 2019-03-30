"""Users app permission module."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Determinates if the user sending the request is the owner of the account he wants to see."""

    def has_object_permission(self, request, view, obj):
        """Returns if the user is owner of the account."""

        return request.user == obj