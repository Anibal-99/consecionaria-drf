from apps.user.models import User
from .serializers import UserSerializer, SignUpSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class UserViewSet(viewsets.ModelViewSet):

    permission_classes=[IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()

class SignUpViewSet(viewsets.ViewSet):

    serializer_class=SignUpSerializer

    def create(self, request):
        signUp_serializer=self.serializer_class(data=request.data)

        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return Response(signUp_serializer.data, status=status.HTTP_201_CREATED)
        return Response(signUp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
