from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PayoutRuleViewSet

app_name = 'payout_rule'

router = DefaultRouter()
router.register(r'rules', PayoutRuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]