from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Dashboard(request):
    if request.session['role']=='agent':
        return render(request,'agent/Dashboard.html')
    else:
        return redirect("../agency/logout")
    
    
