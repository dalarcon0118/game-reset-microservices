from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Role, UserRole
from .serializers import RoleSerializer, UserRoleSerializer
from django.contrib.auth.models import User

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    @action(detail=True, methods=['post'])
    def assign_users(self, request, pk=None):
        role = self.get_object()
        user_ids = request.data.get('user_ids', [])
        
        assignments = []
        for user_id in user_ids:
            try:
                user = User.objects.get(id=user_id)
                user_role, created = UserRole.objects.get_or_create(
                    user=user,
                    role=role,
                    defaults={'is_active': True}
                )
                assignments.append(user_role)
            except User.DoesNotExist:
                continue

        serializer = UserRoleSerializer(assignments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        role = self.get_object()
        user_roles = UserRole.objects.filter(role=role, is_active=True)
        serializer = UserRoleSerializer(user_roles, many=True)
        return Response(serializer.data)

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

    @action(detail=False, methods=['get'])
    def user_roles(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            user_roles = UserRole.objects.filter(user_id=user_id, is_active=True)
            serializer = self.get_serializer(user_roles, many=True)
            return Response(serializer.data)
        return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
