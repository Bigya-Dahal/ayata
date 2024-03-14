from django.shortcuts import render
from rest_framework import viewsets
from team.models import *
from team.serializers import *

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer