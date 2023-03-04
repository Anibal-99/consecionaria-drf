from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.car_commerce.api.serializers import *
from apps.car_commerce.models import *
from django.shortcuts import get_object_or_404


class RegionViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset=Region.objects.all()
        region_serializer=RegionSerializer(queryset, many=True)
        return Response(region_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset=Region.objects.all()
        try:
            region=get_object_or_404(queryset, pk=pk)
        except Region.DoesNotExist:
            return Response({'Message':'region does not exist'})

        serializer=RegionSerializer(region)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        region_serializer=RegionSerializer(data=request.data)

        if region_serializer.is_valid():
            region_serializer.save()
            return Response(region_serializer.data, status=status.HTTP_201_CREATED)
        return Response(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        region=get_object_or_404(Region.objects.all(), pk=pk)
        region.delete()
        return Response({'Message': 'region eliminated'}, status=status.HTTP_200_OK)


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class= CountrySerializer
    queryset= Country.objects.all()


class SalesPersonViewSet(viewsets.ModelViewSet):
    serializer_class= SalesPersonSerializer
    queryset=SalesPerson.objects.all()

class CarBrandViewSet(viewsets.ModelViewSet):
    serializer_class=CarBrandSerializer
    queryset=CarBrand.objects.all()

class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class=CarModelSerializer
    queryset=CarModel.objects.all()

class ColorModelViewSet(viewsets.ModelViewSet):
    serializer_class=ColorSerializer
    queryset=Color.objects.all()

class CarViewSet(viewsets.ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class=CustomerSerializer
    queryset=Customer.objects.all()

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class=SaleSerializer
    queryset=Sale.objects.all()
