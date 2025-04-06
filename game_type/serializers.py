from rest_framework import serializers
from .models import GameType

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']