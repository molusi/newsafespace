
from .models import *
from django import forms
from .models import Comment
user = get_user_model()





class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'label':"comment","rows":"1","cols":3,"class":"form-control","placeholder":"add comment..."}))
    class Meta:
        model = Comment
        fields = ['content']
class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'label':"comment","rows":"1","cols":3,"class":"form-control","placeholder":"add comment..."}))
    class Meta:
        model = Comment
        fields = ['content']

class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title','class':' form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":12,"cols":60,'class':' form-control','placeholder':'content'}))



    class Meta:
        model = Article
        fields = ['title','content','image','author']


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title','class':' form-control'}))
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': ' form-control'}))

    class Meta:
        model = Article
        exclude = ['author',"votes","comments_all"]





class UserProfileForm(forms.Form):
    preferred_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'preffered name', 'class': 'form-control'}), max_length=255)
    about = forms.CharField(widget=forms.Textarea(attrs={"rows":3,"cols":25,"placeholder":"About you..","class":"form-control"}),max_length=400)
    linkedin = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'url', 'class': ' form-control'}), max_length=255)

    class Meta:
        model = Userprofile
        fields = ['preferred_name','profilepic','about','user','linkedin']

class UserProfileUpdateForm(forms.ModelForm):
    preferred_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'preffered name', 'class': 'px-2 form-control'}), max_length=255)
    about = forms.CharField(widget=forms.Textarea(attrs={"rows":3,"cols":25,"placeholder":"About you..","class":"form-control"}),max_length=400)
    class Meta:
        model = Userprofile
        fields = ['preferred_name','profilepic','about','linkedin']
        
