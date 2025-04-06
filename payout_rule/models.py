from django.db import models
from game_type.models import GameType
from structure.models import Structure

class PayoutRule(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name='payout_rules')
    payout_rate = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.JSONField(help_text="JSON defining the winning condition")
    owner_structure = models.ForeignKey(
        Structure,
        on_delete=models.CASCADE,
        limit_choices_to={'node_type': 'bank'},
        related_name='payout_rules'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['game_type', '-created_at']
        unique_together = ['game_type', 'condition', 'owner_structure']

    def __str__(self):
        return f"Payout Rule {self.id} - {self.game_type.name} ({self.payout_rate}x)"
