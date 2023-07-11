from django.contrib import admin

from django.contrib import admin
from . models import *
User=get_user_model()



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created')


class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('preffered_name','user','profilepic')






admin.site.register(Article,ArticleAdmin)
admin.site.register(Userprofile,UserprofileAdmin)

