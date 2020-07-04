from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

# Create your models here.

class CreateAgency(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    AgencyName=models.CharField(max_length=200,null=False, blank=False)
    Logo=models.ImageField(upload_to='AgencyAssets')
    HeadOfficeAddress=models.TextField(null=False, blank=False)
    Phone=PhoneNumberField(null=False, blank=False, unique=True)
    Email = models.EmailField(max_length=70, null=False, blank=False, unique=True)
    AgencyDescription=models.TextField(null=False, blank=False)
    CRNumber=models.IntegerField(null=False, blank=False)
    SupportingDocument=models.FileField(upload_to='AgencyAssets')
    SupportingDocumentExpiry=models.DateField()
    Active=models.BooleanField(default=False)
    PaymentRequired=models.BooleanField(default=True)
    PaymentExpiry=models.DateField(null=True,blank=True)
    NewRequest=models.BooleanField(default=True)
    Roles=models.CharField(max_length=20,null=False, blank=False,default='agency')

    def __str__(self):
       return self.AgencyName
    
    
class Agent(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Agency=models.ForeignKey(CreateAgency, on_delete=models.CASCADE)
    Name=models.CharField(max_length=200,null=False, blank=False)
    Image=models.ImageField(upload_to='AgencyAssets')
    Nationality=models.CharField(max_length=200,null=False, blank=False)
    Languages=models.TextField(null=False, blank=False)
    OfficeAddress=models.TextField(null=False, blank=False)
    Phone=PhoneNumberField(null=False, blank=False, unique=True)
    Email = models.EmailField(max_length=70, null=False, blank=False, unique=True)
    Description=models.TextField(null=False, blank=False)
    Active=models.BooleanField(default=False)
    Roles=models.CharField(max_length=20,null=False, blank=False,default='agent')


    def save(self):
        super().save()
        img = Image.open(self.Image.path)
        if img.height>300 or img.weight>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Image.path)

    def __str__(self):
       return self.Name

        


