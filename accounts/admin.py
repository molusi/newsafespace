from django.contrib import admin
from django.contrib import admin
from .models import *
from .forms import *
import datetime
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

admin.site.site_header = "Kay's thisnthat Admin"
admin.site.site_title= "Kay's thisnthat Admin Area"
admin.site.index_title = "Welcome to Kay's thisnthat admin area"

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = User


admin.site.register(User,UserAdmin)