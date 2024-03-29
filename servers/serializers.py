from rest_framework import serializers
from .models import Server

class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('name', 'user_name', 'mac_address')