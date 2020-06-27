from django.db import models

# Create your models here.
class Mainlocation(models.Model):
    MainLocationName=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.TextField(null=False, blank=False)

    def __str__(self):
       return self.MainLocationName

class Sublocation(models.Model):
    MainLocationName=models.ForeignKey(Mainlocation, on_delete=models.CASCADE)
    SubLocationName=models.CharField(max_length=200,null=False, blank=False,unique=True)
    Description=models.TextField(null=False, blank=False)

    def __str__(self):
       return self.SubLocationName
   
   