from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#TUTORIAL

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def client_list(request):
	"""
	List of all the clients in the database.
	"""
	if request.method == 'GET':
		clients = Client.objects.all()
		serializer = ClientSerializer(clients, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ClientSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def client_detail(request, pk):
	"""
	Retrieve, update or delete a client.
	"""

	try:
		client = Client.objects.get(pk=pk)
	except Client.DoestNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ClientSerializer(client)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ClientSerializer(client, data= data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)
	elif request.method == 'DELETE':
		client.delete()
		return HttpResponse(status=204)



