from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import NumberLimitRule
from .serializers import NumberLimitRuleSerializer

class NumberLimitRuleViewSet(viewsets.ModelViewSet):
    queryset = NumberLimitRule.objects.all()
    serializer_class = NumberLimitRuleSerializer

    def get_queryset(self):
        queryset = NumberLimitRule.objects.all()
        draw_id = self.request.query_params.get('draw', None)
        game_type_id = self.request.query_params.get('game_type', None)
        is_active = self.request.query_params.get('is_active', None)
        owner_structure_id = self.request.query_params.get('owner_structure', None)

        if draw_id:
            queryset = queryset.filter(draw_id=draw_id)
        if game_type_id:
            queryset = queryset.filter(game_type_id=game_type_id)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        if owner_structure_id:
            queryset = queryset.filter(owner_structure_id=owner_structure_id)

        return queryset

    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        rule = self.get_object()
        rule.is_active = not rule.is_active
        rule.save()
        
        serializer = self.get_serializer(rule)
        return Response(serializer.data)
