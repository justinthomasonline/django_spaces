from django.contrib import admin
from .models import RentBuy,PropertyType,TimePeriod,Furnishing,Amenities,Property,PropertyAminities,PropertyImages

# Register your models here.
admin.site.register(RentBuy)
admin.site.register(PropertyType)
admin.site.register(TimePeriod)
admin.site.register(Furnishing)
admin.site.register(Amenities)
admin.site.register(Property)
admin.site.register(PropertyAminities)
admin.site.register(PropertyImages)
