from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from .serializer import HotelSerializer
from .models import Hotel

# Create your views here.
@api_view(['GET'])
def hotel(request):
    my_data = Hotel.objects.all()
    serializer = HotelSerializer(my_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_data(request):
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_hotel(request, id):
    id = Hotel.objects.get(id=id)
    hotel = HotelSerializer(id, data=request.data)
    if hotel.is_valid():
        hotel.save()
        return Response(hotel.data)
    return Response(hotel.errors)
 

@api_view(['DELETE'])
def delete_hotel(request, id):
        hotel = Hotel.objects.get(id=id)
        hotel.delete()
        return Response('deleted successfully!')


@api_view(['PATCH'])
def update_hotel_data(request, id):
    id = Hotel.objects.get(id=id)
    hotel = HotelSerializer(id, data=request.data, partial=True)
    if hotel.is_valid():
        hotel.save()
        return Response(hotel.data)
    return Response(hotel.errors)