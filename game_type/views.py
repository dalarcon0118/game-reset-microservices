from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import GameType
from .serializers import GameTypeSerializer

class GameTypeViewSet(viewsets.ModelViewSet):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer

    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        game_type = self.get_object()
        game_type.is_active = not game_type.is_active
        game_type.save()
        serializer = self.get_serializer(game_type)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = GameType.objects.all()
        active_only = self.request.query_params.get('active', None)
        if active_only is not None:
            queryset = queryset.filter(is_active=active_only.lower() == 'true')
        return queryset
