from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from .views import UserViewset


router = DefaultRouter(trailing_slash=False)
router.register(r'signup', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login', ObtainAuthToken.as_view()),
]