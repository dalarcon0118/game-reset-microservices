from rest_framework import serializers
from .models import Origin

class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ['id', 'name', 'code', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']