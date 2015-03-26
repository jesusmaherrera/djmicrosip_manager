from django.shortcuts import render

from rest_framework import viewsets
from .models import ClientApplication
from .serializers import ClientApplicationSerializer

class ClientApplicationViewSet(viewsets.ModelViewSet):
    queryset = ClientApplication.objects.all()
    serializer_class = ClientApplicationSerializer
    filter_fields = ('id',)
    paginate_by = 1