from django.contrib import admin
from .models import PayoutRule

@admin.register(PayoutRule)
class PayoutRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_type', 'payout_rate', 'owner_structure', 'is_active')
    list_filter = ('game_type', 'is_active', 'owner_structure__name')
    search_fields = ('id', 'game_type__name', 'owner_structure__name')
