
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import Permission, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class CreateuserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input','id':'email-input','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','id':'password-input','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['email','password1','password2']



class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input','id':'email-input','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','id':'password-input','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['email','password']
