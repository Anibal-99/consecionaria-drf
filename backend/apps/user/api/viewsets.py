from apps.user.models import User
from .serializers import UserSerializer, SignUpSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate

class UserViewSet(viewsets.ModelViewSet):

    permission_classes=[IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()

class SignUpViewSet(viewsets.ViewSet):
    """View para realiar un signup de un usuario"""

    serializer_class=SignUpSerializer

    def create(self, request):
        signUp_serializer=self.serializer_class(data=request.data)

        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return Response(signUp_serializer.data, status=status.HTTP_201_CREATED)
        return Response(signUp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    permission_classes=[]
    """
    En este método, se crea un diccionario llamado
    content que contiene dos claves: "user" y "auth". La clave "user"
    se establece como una cadena que representa el usuario actual de
    la solicitud (request.user) y la clave "auth" se establece como
    una cadena que representa el
    token de autenticación actual de la solicitud (request.auth).
    """
    def list(self, request):
        content={
            "user":str(request.user),
            "auth": str(request.auth)
        }

        return Response(content, status=status.HTTP_200_OK)

    def create(self, request):
        """ ahora buscamos el objeto user al que pertenecen estas credenciales de email
        y password o cualquier otro atributo que queramos para el login"""
        username_data=request.data.get("username")
        password_data=request.data.get("password")

        user=authenticate(username=username_data,password=password_data) # si falla la autenticacion devuevle None

        if user is not None:
            response={
                "Message":"Login Successfull",
                "token": user.auth_token.key
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"Invalid email or password"})
