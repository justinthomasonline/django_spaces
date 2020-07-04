from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from properties.forms import CreateProperty,ImageForms,NearbyForms
from .models import Property,PropertyImages,PropertyNearby
from propertymeta.models import Amenities,PropertyType,Sublocation
from django.forms import modelformset_factory
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core import serializers


# Create your views here.
@login_required
def AddProperty(request):
    if request.session['role']=='agent':
        if request.method=='POST':
             propertyform =  CreateProperty(request.POST,use_required_attribute=False)
             selectedaminities = request.POST.getlist('aminities')
            

             if propertyform.is_valid():
                
                 return HttpResponse('Valid')
             else:
                 print (propertyform.cleaned_data['propertyaminity'])
                 data = {}
                 formset = modelformset_factory(PropertyImages,form=ImageForms)
                 imgformset = formset(queryset=PropertyImages.objects.none(),prefix='image')

                 formnearbyset =modelformset_factory(PropertyNearby,form=NearbyForms)
                 nearbyformset = formnearbyset(queryset=PropertyNearby.objects.none(),prefix='nearby')
            
                 aminities =  Amenities.objects.all()
                 data['title']='Create Property'
                 content = {'p_form':propertyform, 'imgformset':imgformset,'nearbyformset':nearbyformset,'aminities':aminities,'data':data}
                 return render(request, 'property/create.html',content)

                 

        else:
            propertyform =  CreateProperty(use_required_attribute=False)
            formset = modelformset_factory(PropertyImages,form=ImageForms)
            imgformset = formset(queryset=PropertyImages.objects.none(),prefix='image')

            formnearbyset =modelformset_factory(PropertyNearby,form=NearbyForms)
            nearbyformset = formnearbyset(queryset=PropertyNearby.objects.none(),prefix='nearby')
           
            aminities =  Amenities.objects.all()
            data = {}
            data['title']='Create Property'
            content = {'p_form':propertyform, 'imgformset':imgformset,'nearbyformset':nearbyformset,'aminities':aminities,'data':data}
            return render(request, 'property/create.html',content)
            
    else:
        return redirect('AgencyLogout')


@login_required
def Ajaxgetproperttype(request):
    value = request.GET['value'] 
    if value == '1' or value == '2':
        propertytype = PropertyType.objects.filter(Q(RentBuyType_id=1) | Q(RentBuyType_id=2))
    else:
        propertytype = PropertyType.objects.filter(Q(RentBuyType_id=3) | Q(RentBuyType_id=4))

    result_json = serializers.serialize('json', propertytype)

    return HttpResponse(result_json, content_type='application/json')  


@login_required
def Ajaxgetsublocation(request):
    value = request.GET['value'] 
    Sublocations =  Sublocation.objects.filter(MainLocationName_id=value)

    result_json = serializers.serialize('json', Sublocations)

    return HttpResponse(result_json, content_type='application/json')  
 
        





