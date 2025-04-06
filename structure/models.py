from django.db import models
from tenant_schemas.models import TenantMixin
from tenants.models import Client

class Structure(models.Model):
    NODE_TYPE_CHOICES = [
        ('bank', 'Bank'),
        ('branch', 'Branch'),
        ('other', 'Other')
    ]
    
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='structures')
    name = models.CharField(max_length=255)
    node_type = models.CharField(max_length=20, choices=NODE_TYPE_CHOICES, default='branch')
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    level = models.IntegerField(default=0)
    path = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('name', 'parent', 'tenant')
        ordering = ['path']

    def __str__(self):
        return self.path
