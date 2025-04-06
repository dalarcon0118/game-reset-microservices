from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameTypeViewSet

app_name = 'game_type'

router = DefaultRouter()
router.register(r'game-types', GameTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]