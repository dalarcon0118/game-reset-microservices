from rest_framework import serializers
from .models import NumberLimitRule
from draw.serializers import DrawSerializer
from game_type.serializers import GameTypeSerializer
from structure.serializers import StructureSerializer

class NumberLimitRuleSerializer(serializers.ModelSerializer):
    draw_details = DrawSerializer(source='draw', read_only=True)
    game_type_details = GameTypeSerializer(source='game_type', read_only=True)
    owner_structure_details = StructureSerializer(source='owner_structure', read_only=True)

    class Meta:
        model = NumberLimitRule
        fields = [
            'id', 'draw', 'game_type', 'numbers', 'max_total_amount', 
            'owner_structure', 'created_at', 'updated_at', 'is_active',
            'draw_details', 'game_type_details', 'owner_structure_details'
        ]
        read_only_fields = ['created_at', 'updated_at']