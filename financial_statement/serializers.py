from rest_framework import serializers
from .models import FinancialStatement
from draw.serializers import DrawSerializer

class FinancialStatementSerializer(serializers.ModelSerializer):
    draw_details = DrawSerializer(source='draw', read_only=True)
    structure_id = serializers.IntegerField(source='object_id')
    
    class Meta:
        model = FinancialStatement
        fields = [
            'id', 'draw', 'structure_id', 'total_collected', 
            'total_paid', 'net_result', 'created_at', 'last_updated',
            'draw_details'
        ]
        read_only_fields = ['net_result', 'created_at', 'last_updated']