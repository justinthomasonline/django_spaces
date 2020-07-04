from django.contrib import admin
from .models import Mainlocation,Sublocation,RentBuy,PropertyType,TimePeriod,Furnishing,Amenities

# Register your models here.
admin.site.register(Mainlocation)
admin.site.register(Sublocation)
admin.site.register(RentBuy)
admin.site.register(PropertyType)
admin.site.register(TimePeriod)
admin.site.register(Furnishing)
admin.site.register(Amenities)



