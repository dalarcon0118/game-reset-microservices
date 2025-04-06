from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Bet
from .serializers import BetSerializer

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    def get_queryset(self):
        queryset = Bet.objects.all()
        draw_id = self.request.query_params.get('draw', None)
        game_type_id = self.request.query_params.get('game_type', None)
        is_winner = self.request.query_params.get('is_winner', None)
        owner_structure_id = self.request.query_params.get('owner_structure', None)

        if draw_id:
            queryset = queryset.filter(draw_id=draw_id)
        if game_type_id:
            queryset = queryset.filter(game_type_id=game_type_id)
        if is_winner is not None:
            queryset = queryset.filter(is_winner=is_winner.lower() == 'true')
        if owner_structure_id:
            queryset = queryset.filter(owner_structure_id=owner_structure_id)

        return queryset

    @action(detail=True, methods=['post'])
    def mark_as_winner(self, request, pk=None):
        bet = self.get_object()
        payout_amount = request.data.get('payout_amount', 0)
        
        bet.is_winner = True
        bet.payout_amount = payout_amount
        bet.save()
        
        serializer = self.get_serializer(bet)
        return Response(serializer.data)