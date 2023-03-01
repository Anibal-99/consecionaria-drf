from django.urls import path, include
#from apps.car_commerce.api.views import region_list, region_detail
from apps.car_commerce.api.views import RegionListApiView, RegionDetailApiView
from .routers import router

urlpatterns = [
    #path('list/',  RegionListApiView.as_view(), name='list_region'),
    #path('detail/<int:pk>', RegionDetailApiView.as_view(), name='detail_region'),
    path('', include(router.urls)),
]
