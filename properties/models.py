from django.db import models
from django.contrib.auth.models import User
from propertymeta.models import RentBuy,PropertyType,TimePeriod,Furnishing,Mainlocation,Sublocation
from datetime import datetime

# Create your models here.

class Property(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    PropertyID=models.CharField(max_length=255,null=False, blank=False,unique=True)
    PropertyTitle=models.CharField(max_length=500,null=False, blank=False)
    PropertyTitleMeta=models.CharField(max_length=500,null=False, blank=False)
    YearBuilt=models.DateField()
    RentBuy=models.ForeignKey(RentBuy,null=False, blank=False, on_delete=models.CASCADE)
    PropertyType=models.ForeignKey(PropertyType,null=False, blank=False, on_delete=models.CASCADE)
    TimePeriod=models.ForeignKey(TimePeriod,null=False, blank=False, on_delete=models.CASCADE)
    Furnishing=models.ForeignKey(Furnishing,null=False, blank=False, on_delete=models.CASCADE)
    Price=models.DecimalField(max_digits=15, decimal_places=5, blank=False, null=False)
    Floor=models.IntegerField(null=False, blank=False)
    Area=models.IntegerField(null=False, blank=False)
    BedRoom=models.IntegerField(null=True, blank=True)
    BathRoom=models.IntegerField(null=True, blank=True)
    Video=models.URLField(max_length=500,null=True, blank=True)
    MainLocation=models.ForeignKey(Mainlocation,null=False, blank=False, on_delete=models.CASCADE)
    SubLocation=models.ForeignKey(Sublocation,null=False, blank=False, on_delete=models.CASCADE)
    About=models.TextField(null=False, blank=False)
    Address=models.TextField(null=False, blank=False)
    Latitude=models.DecimalField(max_digits=9, decimal_places=6)
    Longitude=models.DecimalField(max_digits=9, decimal_places=6)
    Status=models.BooleanField(default=True)
    propertyaminity=models.CharField(max_length=500,null=True, blank=True)
    CreatedOn=models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.PropertyTitle       


class PropertyNearby(models.Model):
    NearbyType=models.CharField(max_length=200,null=False, blank=False)
    Distance=models.CharField(max_length=200,null=False, blank=False)
    Property=models.ForeignKey(Property, on_delete=models.CASCADE)

class PropertyImages(models.Model):
    PropertyImageType=models.CharField(max_length=200,null=False, blank=False)
    PropertyImage=models.ImageField(upload_to='PropertyAsset')
    Property=models.ForeignKey(Property, on_delete=models.CASCADE)


    
