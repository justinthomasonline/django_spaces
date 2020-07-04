from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Mainlocation(models.Model):
    MainLocationName=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.MainLocationName

class Sublocation(models.Model):
    MainLocationName=models.ForeignKey(Mainlocation, on_delete=models.CASCADE)
    SubLocationName=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.SubLocationName

class RentBuy(models.Model):
    Type=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.Type

class PropertyType(models.Model):
    RentBuyType=models.ForeignKey(RentBuy, on_delete=models.CASCADE)
    Type=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.Type


class TimePeriod(models.Model):
    Type=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.Type

class Furnishing(models.Model):
    Type=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.Type

class Amenities(models.Model):
    Type=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
       return self.Type
