from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({
                'status': 'success',
                'data': {
                    'access_token': response.data['access'],
                    'refresh_token': response.data['refresh'],
                    'token_type': 'Bearer',
                    'expires_in': 3600  # 1 hour in seconds
                },
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        return response
