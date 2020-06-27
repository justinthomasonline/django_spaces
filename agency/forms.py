from django import forms
from .models import CreateAgency,Agent,User 

class DateInput(forms.DateInput):
    input_type = 'date'


class AgencyRegisterForm(forms.ModelForm):
    class Meta:
        model = CreateAgency
        fields = ('AgencyName','Logo','HeadOfficeAddress','Phone','Email','AgencyDescription','CRNumber','SupportingDocument','SupportingDocumentExpiry')
        labels  = {
        'AgencyName':'Agency Name', 
        'HeadOfficeAddress':'Head Office Address', 
        'SupportingDocument':'Supporting documents like CR, contract etc',
        'SupportingDocumentExpiry':'Expiry date of the document',
        'AgencyDescription':'About Agency'
        }
        widgets = {
            'AgencyName'  : forms.TextInput(attrs={'class':'form-control py-4'}),
            'Logo'  : forms.FileInput(attrs={'class':'form-control py-4'}),
            'HeadOfficeAddress'  : forms.TextInput(attrs={'class':'form-control py-4'}),
            'Email':forms.EmailInput(attrs={'class':'form-control py-4'}),
            'Phone':forms.TextInput(attrs={'class':'form-control py-4'}),
            'AgencyDescription':forms.Textarea(attrs={'class':'form-control py-4' , 'rows': 4, 'cols': 10}),
            'CRNumber':forms.NumberInput(attrs={'class':'form-control py-4'}),
            'SupportingDocument':forms.FileInput(attrs={'class':'form-control py-4'}),
            'SupportingDocumentExpiry':DateInput(attrs={'class':'form-control py-4'}),
             }


class AgentRegisterForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('Name','Image','Nationality','Languages','OfficeAddress','Phone','Email','Description')
        labels  = {
        'Name':'Agent Name *', 
        'OfficeAddress':'Office Address *', 
        'Description':'About Agent *',
        'Image' : 'Image *',
        'Nationality' : 'Nationality *',
        'Languages' : 'Languages *',
        'Email' :'Email *',
        'Phone' : 'Phone *',
        'Description' : 'Description *'


        }
        widgets = {
            'Name'  : forms.TextInput(attrs={'class':'form-control py-4'}),
            'Image'  : forms.FileInput(attrs={'class':'form-control py-4'}),
            'Nationality' : forms.TextInput(attrs={'class':'form-control py-4'}),
            'Languages' : forms.TextInput(attrs={'class':'form-control py-4'}),
            'OfficeAddress'  : forms.TextInput(attrs={'class':'form-control py-4'}),
            'Email':forms.EmailInput(attrs={'class':'form-control py-4'}),
            'Phone':forms.TextInput(attrs={'class':'form-control py-4'}),
            'Description':forms.Textarea(attrs={'class':'form-control py-4' , 'rows': 4, 'cols': 10}),
                }

                

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields = ('username','password')

        labels  = {
        'username':'Agent username *', 
        'password':'Agent Password *', 
        
        }
       
        widgets = {
            'username'  : forms.TextInput(attrs={'class':'form-control py-4'}),
            'password'  : forms.PasswordInput(attrs={'class':'form-control py-4'}),
                  }                




    
