from django.contrib import admin
from .models import NumberLimitRule

@admin.register(NumberLimitRule)
class NumberLimitRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_type', 'draw', 'numbers', 'max_total_amount', 'owner_structure', 'is_active')
    list_filter = ('game_type', 'is_active', 'owner_structure__name')
    search_fields = ('id', 'game_type__name', 'owner_structure__name')
    raw_id_fields = ('draw', 'game_type', 'owner_structure')
