from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from property.forms import CreateProperty,ImageForms
from .models import Amenities,PropertyImages
from django.forms import modelformset_factory
# Create your views here.

def AddProperty(request):
    if request.session['role']=='agent':
        if request.method=='POST':
             propertyform =  CreateProperty(request.POST)
             selectedaminities = request.POST.getlist('aminities')
             print(selectedaminities)
             

             if propertyform.is_valid():
                 return HttpResponse('Valid')
             else:
                 return HttpResponse('Not Valid')

        else:
            propertyform =  CreateProperty(use_required_attribute=False)
            formset = modelformset_factory(PropertyImages,form=ImageForms)
            imgformset = formset(queryset=PropertyImages.objects.none(),prefix='image')
            aminities =  Amenities.objects.all()
            data = {}
            data['title']='Create Property'
            content = {'p_form':propertyform, 'imgformset':imgformset,'aminities':aminities,'data':data}
            return render(request, 'property/create.html',content)
            
    else:
        return redirect('AgencyLogout')


