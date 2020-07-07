from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
#from crispy_forms.helper import FormHelper

class UserRegisterForm(UserCreationForm):
    #helper = FormHelper()
    #helper.show_labels = False
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    #helper = FormHelper()
    #helper.show_labels = False
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    #helper = FormHelper()
    #helper.show_labels = False
    bio = forms.Textarea()
    image = forms.ImageField(required=False)
    class Meta:
        model = Profile 
        fields = ['image','bio','bg_img']


