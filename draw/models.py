from django.db import models
from structure.models import Structure
from origin.models import Origin
from winning_record.models import WinningRecord

class Draw(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    draw_datetime = models.DateTimeField()
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, related_name='draws')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    owner_structure = models.ForeignKey(
        Structure,
        on_delete=models.CASCADE,
        limit_choices_to={'node_type': 'bank'},
        related_name='draws'
    )
    winning_numbers = models.OneToOneField(
        WinningRecord,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='draw'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-draw_datetime']

    def __str__(self):
        return f"Draw {self.id} - {self.draw_datetime}"
