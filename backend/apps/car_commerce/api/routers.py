from .viewsets import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

#router.register('region', RegionViewSet, basename='region')
#router.register('country', CountryViewSet, basename='country')
router.register('sales_person', SalesPersonViewSet, basename='sales_person')
router.register('car_brand', CarBrandViewSet, basename='car_brand')
router.register('car_model', CarModelViewSet, basename='car_model')
router.register('color', ColorViewSet, basename='color')
router.register('car', CarViewSet, basename='car')
router.register('sale', SaleViewSet, basename='sale')
