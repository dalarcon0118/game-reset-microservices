from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OriginViewSet

app_name = 'origin'

router = DefaultRouter()
router.register(r'origins', OriginViewSet)

urlpatterns = [
    path('', include(router.urls)),
]