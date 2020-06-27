from django.urls import path
from . import views

urlpatterns =[
    path('addproperty',views.AddProperty, name='AddProperty'), 
   ]