urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/origin/', include('origin.urls')),
    path('api/game-type/', include('game_type.urls')),
    # Add this to your urlpatterns
    path('api/financial-statement/', include('financial_statement.urls')),
]
