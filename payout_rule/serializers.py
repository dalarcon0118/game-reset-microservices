from rest_framework import serializers
from .models import PayoutRule
from game_type.serializers import GameTypeSerializer
from structure.serializers import StructureSerializer

class PayoutRuleSerializer(serializers.ModelSerializer):
    game_type_details = GameTypeSerializer(source='game_type', read_only=True)
    owner_structure_details = StructureSerializer(source='owner_structure', read_only=True)

    class Meta:
        model = PayoutRule
        fields = [
            'id', 'game_type', 'payout_rate', 'condition', 'owner_structure',
            'created_at', 'updated_at', 'is_active', 'game_type_details', 
            'owner_structure_details'
        ]
        read_only_fields = ['created_at', 'updated_at']