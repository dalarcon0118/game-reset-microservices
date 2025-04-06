from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Origin
from .serializers import OriginSerializer

class OriginViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        origin = self.get_object()
        origin.is_active = not origin.is_active
        origin.save()
        serializer = self.get_serializer(origin)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Origin.objects.all()
        active_only = self.request.query_params.get('active', None)
        if active_only is not None:
            queryset = queryset.filter(is_active=active_only.lower() == 'true')
        return queryset
