from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.car_commerce.api.urls')),
    path('api/', include('apps.user.api.urls')),
]
