from rest_framework import serializers
from .models import Structure

class StructureSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Structure
        fields = ['id', 'name', 'description', 'parent', 'level', 'path', 'children', 'created_at', 'updated_at']
        read_only_fields = ['level', 'path', 'tenant']

    def get_children(self, obj):
        children = Structure.objects.filter(parent=obj, tenant=obj.tenant)
        return StructureSerializer(children, many=True).data