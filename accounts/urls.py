
from .views import logmeout
from django.urls import path
from.models import *
from blog import views

app_name='accounts'

urlpatterns = [
    path('',blog.views.person_login,name="person_login"),
    path('login/',blog.views.person_login,name="person_login"),
    path('logout/',logmeout,name='logout'),
    ]