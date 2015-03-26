from rest_framework import serializers
from .models import ClientApplication

class ClientApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientApplication