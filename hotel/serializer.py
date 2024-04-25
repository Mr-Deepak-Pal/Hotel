from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=('id', 'hotel_name', 'hotel_address', 'hotel_star', 'pincode')