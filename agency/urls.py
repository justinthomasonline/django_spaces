from django.urls import path
from . import views

urlpatterns =[
    path('',views.login, name='AgencyLogin'), 
    path('agency/register',views.AgencyRegister, name='AgencyRegister'),
    path('agency/createagent',views.CreateAgent, name='CreateAgent'),
    path('agency/Dashboard',views.Dashboard, name='AgencyDashboard'),
    path('agency/logout',views.logout, name='AgencyLogout'),
]