"""Users app urls mapping"""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import UserManagementViewSet, UserViewSet

# Json Web Tokens
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserManagementViewSet, base_name='users')
router.register(r'users', UserViewSet, base_name='user')

app_name = 'users'

urlpatterns = [
    path('users/login/', TokenObtainPairView.as_view(), name='login'),
    path('', include(router.urls)),
]