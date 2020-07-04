from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from agency.forms import AgencyRegisterForm,AgentRegisterForm,UserForm
from django.contrib.auth.models import User, auth
from agency.models import CreateAgency,Agent
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required




# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST) 
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            current_user = request.user
            if(CreateAgency.objects.filter(user_id=current_user.id).count()!=0):
                request.session['role'] = 'agency'
                return redirect('agency/Dashboard')
            elif(Agent.objects.filter(user_id=current_user.id).count()):
                request.session['role'] = 'agent'
                return redirect('agent/Dashboard')
            else:
                return HttpResponse('Un authorized')    
                             
        else:
            return HttpResponse('not logged')
       
        
    else:
        form=UserForm()
        data = {}
        data['title']='Spaces Login'
        content = {'form':form,'data':data}
        return render(request, 'login.html',content)
        

def AgencyRegister(request):

    if request.method == 'POST':
        form = AgencyRegisterForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponse('Registered')
        else:
            print(form.errors)
            content = {'form':form}
            return render(request, 'agency/register.html',content)
    else:
         
        form =  AgencyRegisterForm()
        return render(request, 'agency/register.html',{'form':form})
        
@login_required
def CreateAgent(request):
    if request.session['role']=='agency':
        
        if request.method == 'POST':
            agent = AgentRegisterForm(request.POST,request.FILES)
            user =  UserForm(request.POST)
            if user.is_valid() and agent.is_valid():
            
                AgencyId = CreateAgency.objects.get(user_id=request.user.id)
                        
                user = user.save(commit=False) 
                user.set_password(user.password)  
                user.save()
            
                agent = agent.save(commit=False)
                agent.Agency_id = AgencyId.id
                agent.user = User.objects.latest('id')
                agent.save()
                return redirect('CreateAgent')
            
            else:
                print(agent.errors)
                print(user.errors)
                data = {}
                data['title']='Create an Agent'
                content = {'agent':agent,'user':user,'data':data}
                return render(request, 'agency/CreateAgent.html',content)
        else:
            
            agent =  AgentRegisterForm(use_required_attribute=False)
            user =   UserForm(use_required_attribute=False)
            data = {}
            data['title'] = 'Create an Agent'
            return render(request, 'agency/CreateAgent.html',{'agent':agent, 'user':user, 'data':data})

    else:
        return redirect("AgencyLogout")


@login_required
def Dashboard(request):
    if request.session['role']=='agency':
        return render(request,'agency/Dashboard.html')
    else:
        return redirect('AgencyLogout')


   


def logout(request):
    del request.session['role']
    django_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/") 