from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, UserRoleViewSet

app_name = 'roles'

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'user-roles', UserRoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]