
from django.shortcuts import render,redirect,get_object_or_404

from .forms import *

from django.contrib import messages, auth

User = get_user_model()


def logmeout(request):
    auth.logout(request)
    return redirect('blog:home')

# <i class="fa-solid fa-thumbs-down"></i>
# <i class="fa-solid fa-thumbs-up">
# <i class="fa-solid fa-pen-to-square"></i>