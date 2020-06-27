from django import forms
from .models import Property,PropertyAminities,PropertyImages,Amenities

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateProperty(forms.ModelForm):
     class Meta:
          model = Property
          fields =('PropertyID','PropertyTitle','PropertyTitleMeta','YearBuilt','RentBuy',
          'PropertyType','TimePeriod','Furnishing','Price','Floor','Area','BedRoom','BathRoom',
          'Video','MainLocation','SubLocation','About','Address','Latitude','Longitude','Status',
          'CreatedOn')

          FlOOR_CHOICES = (
                    (0,"Ground Floor"),
                    (1,"Frist Floor"),
                    (2,"Second Floor"),
                    (3,"Third Floor"),
                    (4,"Fourth Floor"),
                    (5,"Fifth Floor"),
                    (6,"Sixth Floor"),
                    (7,"Seventh Floor"),
                    (8,"Eightth Floor"),
                    (9,"Nineth Floor"),
                    (10,"Tenth Floor"),
                         )

          widgets = {
              'PropertyID'  : forms.TextInput(attrs={'class':'form-control'}),
              'PropertyTitle'  : forms.TextInput(attrs={'class':'form-control'}),
              'PropertyTitleMeta':forms.TextInput(attrs={'class':'form-control'}),
              'YearBuilt':forms.TextInput(attrs={'class':'form-control'}),
              'RentBuy':forms.Select(attrs={'class':'form-control'}),
              'PropertyType':forms.Select(attrs={'class':'form-control'}),
              'TimePeriod':forms.Select(attrs={'class':'form-control'}),
              'Furnishing':forms.Select(attrs={'class':'form-control'}),
              'Price':forms.NumberInput(attrs={'class':'form-control'}),
              'Floor':forms.Select(choices=FlOOR_CHOICES,attrs={'class': 'form-control'}),
              'Area' :forms.NumberInput(attrs={'class':'form-control'}),
              'BedRoom' :forms.NumberInput(attrs={'class':'form-control'}),
              'BathRoom' :forms.NumberInput(attrs={'class':'form-control'}),
              'Video' :forms.TextInput(attrs={'class':'form-control'}),
              'MainLocation' :forms.Select(attrs={'class':'form-control'}),
              'SubLocation' :forms.Select(attrs={'class':'form-control'}),
                  }

          labels  = {
        'PropertyID':'Property reference number * ', 
        'PropertyTitle':'Title of the property *', 
        'PropertyTitleMeta':'Sub title *',
        'YearBuilt':'property developed year *',
        'RentBuy':'Business type of the property *',
        'PropertyType' : 'Type of the property *',
        'TimePeriod' : 'Tendure of the property*',
        'Furnishing' : 'Status of the property *',
        'Price' : 'Price of the property *',
        'Floor' : 'Floor of the property *',
        'Area' : 'Total area of the property *',
        'BedRoom' : 'Bedroom capcity *',
        'BathRoom' : 'Bathroom capcity *',
        'Video' : 'Video url of the property ',
        'MainLocation' : 'Main location of the property',
        'SubLocation' : 'Sublocation of the property',
         }

class ImageForms(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields=('PropertyImageType','PropertyImage')
        IMAGE_CHOICES = (
                    (0,"Property Image"),
                    (1,"Floor Plan"),
                    )
        widgets = {
            'PropertyImage':forms.FileInput(attrs={'class':'form-control py-4'}),
            'PropertyImageType':forms.Select(choices=IMAGE_CHOICES,attrs={'class': 'form-control'}),
                    }
        labels  = {
                'PropertyImage' : 'Image', 
                'PropertyImageType' : 'Type',
                    }


 


   



  

         
         
