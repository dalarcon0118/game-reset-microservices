from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Structure
from .serializers import StructureSerializer
from tenant_schemas.utils import get_tenant

class StructureViewSet(viewsets.ModelViewSet):
    serializer_class = StructureSerializer

    def get_queryset(self):
        tenant = get_tenant(self.request)
        return Structure.objects.filter(tenant=tenant)

    def perform_create(self, serializer):
        tenant = get_tenant(self.request)
        serializer.save(tenant=tenant)

    @action(detail=True, methods=['get'])
    def tree(self, request, pk=None):
        instance = self.get_object()
        tenant = get_tenant(request)
        children = Structure.objects.filter(
            tenant=tenant,
            path__startswith=instance.path
        )
        serializer = self.get_serializer(children, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def ancestors(self, request, pk=None):
        instance = self.get_object()
        tenant = get_tenant(request)
        paths = instance.path.split('/')
        ancestors = Structure.objects.filter(
            tenant=tenant,
            name__in=paths
        )
        serializer = self.get_serializer(ancestors, many=True)
        return Response(serializer.data)
