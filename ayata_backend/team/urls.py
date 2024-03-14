from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from team.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register('', UserViewSet)

urlpatterns = router.urls