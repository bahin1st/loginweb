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
from .models import Profile, House

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'phonenumber', 'address_line',
            'postcode', 'email', 'country', 'state_region',
            ]


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'description', 'address', 'price', 'is_for_sale'] 
