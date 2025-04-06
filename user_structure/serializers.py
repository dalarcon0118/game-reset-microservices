from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserStructure

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)

class UserStructureSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = UserStructure
        fields = ('id', 'user', 'structure', 'assigned_at', 'is_active', 'role', 'user_details')
        read_only_fields = ('assigned_at',)