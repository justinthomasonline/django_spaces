from django.contrib import admin
from .models import Property,PropertyNearby,PropertyImages

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyNearby)
admin.site.register(PropertyImages)

