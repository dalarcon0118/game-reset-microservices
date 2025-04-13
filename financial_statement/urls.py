from django.urls import path
from .views import (
    FinancialStatementListCreateView,
    FinancialStatementDetailView,
    FinancialStatementReportView
)

urlpatterns = [
    path('', FinancialStatementListCreateView.as_view(), name='financial-statement-list-create'),
    path('<int:pk>/', FinancialStatementDetailView.as_view(), name='financial-statement-detail'),
    path('report/', FinancialStatementReportView.as_view(), name='financial-statement-report'),
]