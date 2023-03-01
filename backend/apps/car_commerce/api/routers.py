from .viewsets import RegionViewSet, CountryViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('region', RegionViewSet, basename='region')
router.register('country', CountryViewSet, basename='country')
