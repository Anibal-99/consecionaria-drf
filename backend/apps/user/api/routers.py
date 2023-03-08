from rest_framework.routers import DefaultRouter
from .viewsets import *

router=DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('signup', SignUpViewSet, basename='signup')
router.register('login', LoginViewSet, basename='login')
