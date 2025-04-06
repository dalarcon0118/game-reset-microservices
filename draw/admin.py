from django.contrib import admin
from .models import Draw, WinningRecord

@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):
    list_display = ('id', 'draw_datetime', 'origin', 'status', 'owner_structure')
    list_filter = ('status', 'owner_structure__node_type')
    raw_id_fields = ('owner_structure', 'origin')

@admin.register(WinningRecord)
class WinningRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'draw', 'created_at')
