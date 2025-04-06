from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserStructureViewSet

app_name = 'user_structure'

router = DefaultRouter()
router.register(r'assignments', UserStructureViewSet, basename='user-structure')

urlpatterns = [
    path('', include(router.urls)),
]