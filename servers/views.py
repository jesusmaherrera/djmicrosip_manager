from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ServerSerializer
from .models import Server

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer