from django.urls import path
from . import views

urlpatterns =[
    path('addproperty',views.AddProperty, name='AddProperty'),
    path('Ajaxgetproperttype',views.Ajaxgetproperttype, name='Ajaxgetproperttype'),
    path('Ajaxgetsublocation',views.Ajaxgetsublocation, name='Ajaxgetsublocation'), 
   ]
