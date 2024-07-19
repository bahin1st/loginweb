from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
# forms.py
from django import forms
from .models import Profile, House,HouseImage

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'phonenumber', 'address_line',
            'postcode', 'email', 'country', 'state_region','pro_pic',
            ]


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'description', 'address', 'price','status','property_type',
                  'parking_spaces','furnishing_status','balcony','garden','pool','heating_type',
                  'cooling_type','pet_policy','security_features','nearby_amenities','contact_phone',
                  'contact_email','rooms_count',
                  'bathrooms_count','area','floors', 'is_for_sale','pics',] 
        


        
class HouseImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ['image']

HouseImageFormSet = forms.inlineformset_factory(
    House, HouseImage, form=HouseImageForm, extra=3  # adjust `extra` for the number of additional images
)

class HouseFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label='Min Price')
    max_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label='Max Price')
    property_type = forms.ChoiceField(required=False, choices=[('', 'Any')] )
    status = forms.ChoiceField(required=False, choices=[('', 'Any')] )
    min_rooms = forms.IntegerField(required=False, label='Min Rooms')
    max_rooms = forms.IntegerField(required=False, label='Max Rooms')
    min_area = forms.FloatField(required=False, label='Min Area')
    max_area = forms.FloatField(required=False, label='Max Area')