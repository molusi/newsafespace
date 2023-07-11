
from . import views
from .views import *
from django.urls import path
from . models import *


app_name = "yvfoundation"

urlpatterns = [
    path('',views.yvfoundationhome,name='home'),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('about/',views.AboutView.as_view(),name="about"),
    ]
