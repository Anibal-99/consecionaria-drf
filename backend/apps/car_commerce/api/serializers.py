from apps.car_commerce.models import Region, Country
from rest_framework import serializers

class RegionSerializer(serializers.ModelSerializer):
    """crea un serializador en base al modelo region"""
    countries=serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model= Region
        fields=[
            'id',
            'name',
            'countries',
        ]

class CountrySerializer(serializers.ModelSerializer):

    region_id=RegionSerializer

    class Meta:
        model=Country
        fields=[
            'id',
            'name',
            'code',
            'region_id',
        ]

"""
class TestRegionSerializer(serializers.Serializer):
    #podemos crear serializadores que no estan basados en modelos
    #de esta forma podemos ver como funcionan por detrar los serializer basados
    #en modelos
    name=serializers.CharField(max_length=100)

    def validate_name(self, value):
        #cada ves que se ejecuta este serializador y el is valid, lo que hace es fijarse donde
        #encuentra la palabra 'validate_nombreAtributo', cuando encuentra esta forma en una funcion, ejecuta la validacion
        #correspondiente a ese atributo del serializador, sino lo que hace es buscar unicamente la funcion
        #llamada validate donde va a devolver los datos validados
        if 'anita' in value:
            raise serializers.ValidationError('error, no puede existir este nombre en una region')
        return value

    def validate(self, data):
        print('validaciones generales')
        return data

    def create(self, validated_data):
        #Esto es lo que hace un modelSerializer al momento de que validamos los datos
        #y luego hacemos un .save() para guardar los datos que nos llegan por post
        return Region.objects.create(**validated_data)

        #el orm de django con los modelSerializer en ves de poner el modelo
        #lo que hace es return self.model, para hacer referencia al modelo que pasamos
        #en la clase Meta:


    def update(self, instance, validated_data):
        #instance vendria siendo la instancia que le pasamos al serializador
        #al momento de llamarlo
        instance.name= validated_data.get('name', instance.name) # esto es lo que drf internamente con un modelSerializer
        instance.save()
        return instance
"""
