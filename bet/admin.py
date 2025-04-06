from django.contrib import admin
from .models import Bet

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('id', 'draw', 'game_type', 'amount', 'is_winner', 'payout_amount', 'owner_structure')
    list_filter = ('is_winner', 'game_type', 'owner_structure__node_type')
    search_fields = ('id', 'draw__id')
    raw_id_fields = ('draw', 'game_type', 'owner_structure')