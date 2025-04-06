from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from draw.models import Draw

class FinancialStatement(models.Model):
    draw = models.ForeignKey(
        Draw, 
        on_delete=models.CASCADE, 
        related_name='financial_statements'
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model': 'structure'}
    )
    object_id = models.PositiveIntegerField()
    owner_structure = GenericForeignKey('content_type', 'object_id')
    
    total_collected = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    net_result = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-draw__draw_datetime', 'content_type', 'object_id']
        unique_together = ['draw', 'content_type', 'object_id']
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
            models.Index(fields=['draw']),
        ]
        verbose_name = "Financial Statement"
        verbose_name_plural = "Financial Statements"

    def __str__(self):
        return f"Financial Statement - Draw {self.draw_id} - Structure {self.object_id}"
    
    def save(self, *args, **kwargs):
        # Calculate net result before saving
        self.net_result = self.total_collected - self.total_paid
        super().save(*args, **kwargs)
