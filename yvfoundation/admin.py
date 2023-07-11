from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('topic','message')



admin.site.register(Contact,ContactAdmin)