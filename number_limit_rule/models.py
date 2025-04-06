from django.db import models
from draw.models import Draw
from game_type.models import GameType
from structure.models import Structure

class NumberLimitRule(models.Model):
    draw = models.ForeignKey(
        Draw, 
        on_delete=models.CASCADE, 
        related_name='number_limits',
        null=True,
        blank=True
    )
    game_type = models.ForeignKey(
        GameType, 
        on_delete=models.CASCADE, 
        related_name='number_limits',
        null=True,
        blank=True
    )
    numbers = models.JSONField(help_text="Numbers to limit")
    max_total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    owner_structure = models.ForeignKey(
        Structure,
        on_delete=models.CASCADE,
        limit_choices_to={'node_type': 'bank'},
        related_name='number_limits'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Number Limit Rule"
        verbose_name_plural = "Number Limit Rules"

    def __str__(self):
        game = self.game_type.name if self.game_type else "All Games"
        draw_info = f"Draw #{self.draw_id}" if self.draw else "All Draws"
        return f"Limit for {game} ({draw_info}): {self.numbers}"
