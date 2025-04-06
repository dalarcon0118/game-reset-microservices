from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NumberLimitRuleViewSet

app_name = 'number_limit_rule'

router = DefaultRouter()
router.register(r'limits', NumberLimitRuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]