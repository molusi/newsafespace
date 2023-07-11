from django import forms
from .models import *
from django.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import Permission, User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import User
from django.utils import timezone
user = get_user_model()

CATEGORY_CHOICES = (
    ('f','food'),
    ('ft','fitness'),
    ('s','sports'),
    ('c','cars'),
    ('t','travel'),
    ('h','health')
)

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'label':"comment","rows":"1","cols":3,"class":"form-control","placeholder":"add comment..."}))
    class Meta:
        model = Comment
        fields = ['content']

class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title','class':'px-2 form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":12,"cols":60,'class':'px-2 form-control','placeholder':'content'}))



    class Meta:
        model = Article
        fields = ['title','content','category','image','author']


class ArticleModelForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'px-2 form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Article
        exclude = ['author']





class UserProfileForm(forms.Form):
    preffered_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'preffered name','class':'px-2 form-control'}),max_length=255)
    about = forms.CharField(widget=forms.Textarea(attrs={"rows":3,"cols":25,"placeholder":"About you..","class":"px-2 form-control"}),max_length=400)
    job_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'job_title', 'class': 'px-2 form-control'}), max_length=255)
    class Meta:
        model = Userprofile
        fields = ['preffered_name','profilepic','job_title','about','user','twitter','instagram']

class UserProfileUpdateForm(forms.ModelForm):
    preffered_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'preffered name', 'class': 'px-2 form-control'}), max_length=255)
    about = forms.CharField(widget=forms.Textarea(attrs={"rows":3,"cols":25,"placeholder":"About you..","class":"px-2 form-control"}),max_length=400)
    job_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'job_title', 'class': 'px-2 form-control'}), max_length=255)
    class Meta:
        model = Userprofile
        fields = ['preffered_name','profilepic', 'job_title','about','twitter','linkedin','instagram']
        
