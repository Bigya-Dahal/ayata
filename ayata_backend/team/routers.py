from rest_framework import routers
from team.viewsets import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'teams', UserViewSet)

urlpatterns = [
    path('', include('router.urls'))]