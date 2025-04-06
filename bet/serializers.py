from rest_framework import serializers
from .models import Bet
from draw.serializers import DrawSerializer
from game_type.serializers import GameTypeSerializer
from structure.serializers import StructureSerializer

class BetSerializer(serializers.ModelSerializer):
    draw_details = DrawSerializer(source='draw', read_only=True)
    game_type_details = GameTypeSerializer(source='game_type', read_only=True)
    owner_structure_details = StructureSerializer(source='owner_structure', read_only=True)

    class Meta:
        model = Bet
        fields = [
            'id', 'draw', 'game_type', 'numbers_played', 'amount', 
            'created_at', 'is_winner', 'payout_amount', 'owner_structure',
            'draw_details', 'game_type_details', 'owner_structure_details'
        ]
        read_only_fields = ['created_at', 'is_winner', 'payout_amount']