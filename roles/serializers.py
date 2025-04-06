from rest_framework import serializers
from .models import Role, UserRole
from django.contrib.auth.models import User

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class UserRoleSerializer(serializers.ModelSerializer):
    role_details = RoleSerializer(source='role', read_only=True)
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'role', 'assigned_at', 'is_active', 'role_details', 'user_details']

    def get_user_details(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name
        }