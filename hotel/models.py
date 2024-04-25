from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

star = [(1,1),(2,2),(3,3),(4,4),(5,5)]

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=64, default=None, blank=True, null=True)
    hotel_address = models.CharField(max_length=128, default=None, blank=True, null=True)
    hotel_star = models.IntegerField(choices=star)
    pincode = models.BigIntegerField()

    class Meta:
        db_table = 'hotel'