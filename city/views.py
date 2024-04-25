from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from .serializer import CitySerializer
from .models import City

# Create your views here.
@api_view(['GET'])
def city(request):
    my_data = City.objects.all()
    serializer = CitySerializer(my_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_data(request):
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_city(request, id):
	id = City.objects.get(id=id)
	data = CitySerializer(id, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response('Failed')

 

@api_view(['DELETE'])
def delete_city(request, id):
        city = City.objects.get(id=id)
        city.delete()
        return Response('deleted successfully!')

@api_view(['PATCH'])
def patch(request, id):
        item = City.objects.get(id=id)
        serializer = CitySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})