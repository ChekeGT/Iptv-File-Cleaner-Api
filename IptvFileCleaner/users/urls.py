"""Users app urls mapping"""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import UserManagementViewSet

router = DefaultRouter()
router.register(r'users', UserManagementViewSet, base_name='users')

app_name = 'users'

urlpatterns = [
    path('', include(router.urls))
]