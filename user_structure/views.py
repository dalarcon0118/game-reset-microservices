from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from tenant_schemas.utils import get_tenant
from .models import UserStructure
from .serializers import UserStructureSerializer, UserSerializer
from structure.models import Structure

class UserStructureViewSet(viewsets.ModelViewSet):
    serializer_class = UserStructureSerializer

    def get_queryset(self):
        tenant = get_tenant(self.request)
        return UserStructure.objects.filter(structure__tenant=tenant)

    @action(detail=False, methods=['post'])
    def assign_user(self, request):
        tenant = get_tenant(request)
        structure_id = request.data.get('structure')
        user_data = request.data.get('user')
        role = request.data.get('role', 'member')

        try:
            structure = Structure.objects.get(id=structure_id, tenant=tenant)
        except Structure.DoesNotExist:
            return Response({'error': 'Structure not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create user if doesn't exist
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data.get('email', ''),
                'first_name': user_data.get('first_name', ''),
                'last_name': user_data.get('last_name', '')
            }
        )

        if created and 'password' in user_data:
            user.set_password(user_data['password'])
            user.save()

        # Create or update user-structure assignment
        user_structure, created = UserStructure.objects.get_or_create(
            user=user,
            structure=structure,
            defaults={'role': role}
        )

        serializer = self.get_serializer(user_structure)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def structure_users(self, request):
        structure_id = request.query_params.get('structure_id')
        tenant = get_tenant(request)
        
        if not structure_id:
            return Response({'error': 'Structure ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        users = UserStructure.objects.filter(
            structure_id=structure_id,
            structure__tenant=tenant,
            is_active=True
        )
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
