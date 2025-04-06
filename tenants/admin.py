from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'schema_name', 'domain_url', 'paid_until', 'on_trial', 'created_on')
    search_fields = ('name', 'schema_name', 'domain_url')
    list_filter = ('on_trial',)
