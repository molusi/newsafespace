from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, request
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from .models import User
User = get_user_model()


def logmeout(request):
    auth.logout(request)
    return redirect('blog:home')