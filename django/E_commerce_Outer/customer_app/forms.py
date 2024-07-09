from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import UserCreationForm

class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=200, required=False)
    
    class meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' 'passward1', 'passward2')
