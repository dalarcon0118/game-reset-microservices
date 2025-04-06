from django.db import models
from draw.models import Draw
from game_type.models import GameType
from structure.models import Structure

class Bet(models.Model):
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE, related_name='bets')
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name='bets')
    numbers_played = models.JSONField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)
    payout_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    owner_structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        limit_choices_to={'node_type': 'LISTERO'},
        related_name='bets'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Bet {self.id} - Draw {self.draw_id}"
