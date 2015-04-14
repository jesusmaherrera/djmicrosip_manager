from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ClientSerializer
from .models import Client
from clientapplications.models import ClientApplication
from rest_framework import permissions
from rest_framework.response import Response

class GetMyKey(APIView):
    """
    Get the apikey of my apps
    """ 
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, format=None, macaddress=None, computername=None, username=None):
    	from microsip_api.core.crypt import EncoderSIC
        
    	enc = EncoderSIC(
    		macaddress = macaddress,
    		computername = computername,
    		username = username,
    	)
    	key = enc.encrypt()
    	aplicaciones = ClientApplication.objects.filter(client__user = request.user).values_list('application__name', flat=True)
    	appskey = enc.encrypt_key_and_apps(
    		key=key,
    		apps = aplicaciones,
    	)
        return Response({'key':appskey,})

