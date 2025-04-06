from django.contrib import admin
from .models import FinancialStatement

@admin.register(FinancialStatement)
class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'draw', 'content_type', 'object_id', 'total_collected', 
                    'total_paid', 'net_result', 'created_at', 'last_updated')
    list_filter = ('draw', 'content_type')
    search_fields = ('id', 'draw__id', 'object_id')
    readonly_fields = ('net_result', 'created_at', 'last_updated')
    raw_id_fields = ('draw',)
