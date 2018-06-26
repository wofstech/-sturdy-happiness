from django import forms
from django.contrib.auth.models import User
from .models import Myhouses

class MyHouseEditForm(forms.ModelForm):    
    class Meta:        
        model = Myhouses   
        labels = {
            'Landlord_number': "Landlord or House Agent's Phone Number"
        }     
        fields = ('name_of_accomodation', 'type_of_apartment','Number_of_rooms', 'house_rent', 'Landlord_number', 'availability', 'State', 'City_or_town', 'nearest_institution', 'description', 'house_image', 'house_image2', 'house_image3', 'house_image4', 'house_image5', 'house_image6', 'house_image7', 'house_image8', 'house_image9', 'house_image10', 'house_image11', 'house_image12',) 

