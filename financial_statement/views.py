from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from .models import FinancialStatement
from .serializers import FinancialStatementSerializer
from structure.models import Structure

class FinancialStatementViewSet(viewsets.ModelViewSet):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementSerializer

    def get_queryset(self):
        queryset = FinancialStatement.objects.all()
        draw_id = self.request.query_params.get('draw', None)
        structure_id = self.request.query_params.get('structure', None)

        if draw_id:
            queryset = queryset.filter(draw_id=draw_id)
        if structure_id:
            queryset = queryset.filter(object_id=structure_id)

        return queryset
    
    def perform_create(self, serializer):
        structure_id = self.request.data.get('structure_id')
        content_type = ContentType.objects.get_for_model(Structure)
        serializer.save(content_type=content_type, object_id=structure_id)
