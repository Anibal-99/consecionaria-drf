from apps.user.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    """Serializador de todos los datos de un usuario, este sera utilizado solo por un
    usuario administrador"""
    class Meta:
        model= User
        fields='__all__'

class SignUpSerializer(serializers.ModelSerializer):
    """Serializador para realizar el signup de los usuario"""

    email=serializers.EmailField()
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model=User
        fields=[
            'email',
            'username',
            'password',
        ]

    def validate(self, attrs):
        """Metodo para validar que el usuario existe en la base de datos"""
        email_exists=User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError({'Message': 'This email already exists'})
        return super().validate(attrs)

    def create(self, validated_data):
        password=validated_data.pop("password")
        user = super().create(validated_data)

        user.set_password(password) # setea la password y la codifica, para luego guardarlo en la db
        user.save()

        Token.objects.create(user=user)

        return user
