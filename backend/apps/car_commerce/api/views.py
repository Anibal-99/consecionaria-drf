from apps.car_commerce.models import Region
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import RegionSerializer
from rest_framework.views import APIView



class RegionListApiView(APIView):
    #para crear las respuestas HTTP de cada modelo tambien podemos utilizar
    #ApiView, en donde en lugar de utilizar las sentencias if para cada verbo HTTP
    #ApiView tiene definido funciones para hacer el trabajo mas escalable

    def get (self, request):
        region_serializer=RegionSerializer(Region.objects.all(), many=True)
        return Response(region_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        region_serializer=RegionSerializer(data=request.data)

        if region_serializer.is_valid():
            region_serializer.save()
            return Response(region_serializer.data, status=status.HTTP_201_CREATED)
        return Response(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionDetailApiView(APIView):
    def get (self, request, pk):
        print('anda pa alla bobo')

        try:
            region=Region.objects.get(id=pk)
        except Region.DoesNotExist:
            return Response({'Message':'Errors, region does not exist'})

        region_serializer=RegionSerializer(region)
        return Response(region_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        try:
            region=Region.objects.get(id=pk)
        except Region.DoesNotExist:
            return Response({'Message':'Errors'})

        region_serializer=RegionSerializer(region, data=request.data)
        if region_serializer.is_valid():
            region_serializer.save()
            return Response(region_serializer.data, status=status.HTTP_200_OK)
        return Response(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        region=Region.objects.get(id=pk)
        region.delete()
        return Response({'Message':'region eliminated'})


"""
vistas basadas en funciones, haciendo uso del decorador API_VIEW

@api_view(['GET', 'POST'])
def region_list(request):

    if request.method=='GET':
        region=Region.objects.all()
        region_serializer=RegionSerializer(region, many=True)
        return Response(region_serializer.data, status=status.HTTP_200_OK)

    elif request.method=='POST':
        region_serializer=RegionSerializer(data=request.data)
        if region_serializer.is_valid():
            region_serializer.save()
            return Response(region_serializer.data, status=status.HTTP_201_CREATED)
        return Response(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def region_detail(request, pk):
    if request.method=='GET':

        try:
            region=Region.objects.get(id=pk)
        except Region.DoesNotExist:
            return Response({'Message': 'Errors region does not exists'},status=status.HTTP_400_BAD_REQUEST)

        region_serializer=RegionSerializer(region)
        return Response(region_serializer.data, status=status.HTTP_200_OK)

    elif request.method=='PUT':
        region_serializer=RegionSerializer(data=request.data)

        if region_serializer.is_valid():
            region_serializer.save()
            return Response(region_serializer.data, status=status.HTTP_201_CREATED)
        return Response(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        Region.objects.get(id=pk).delete()
        return Response({'Message':'Region eliminated'})
"""
