from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BetViewSet

app_name = 'bet'

router = DefaultRouter()
router.register(r'bets', BetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]