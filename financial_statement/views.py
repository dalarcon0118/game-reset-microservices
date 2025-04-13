from rest_framework import generics
from .models import FinancialStatement
from .serializers import FinancialStatementSerializer

class FinancialStatementListCreateView(generics.ListCreateAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementSerializer

class FinancialStatementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementSerializer

class FinancialStatementReportView(generics.ListAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Add any custom filtering for reports
        return queryset
