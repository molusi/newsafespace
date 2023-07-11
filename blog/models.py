from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField


import accounts.models
from accounts.models import User
user = get_user_model()
CATEGORY_CHOICES = (
    ('f','food'),
    ('ft','fitness'),
    ('s','sports'),
    ('c','cars'),
    ('t','travel'),
    ('h','health')
)


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('blog_image',blank=True,null=True)
    content = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    author = models.ForeignKey("Userprofile",on_delete=models.SET_NULL,blank=True,null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk': self.id})

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    author = models.ForeignKey("Userprofile",on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    hide = models.BooleanField(default=False)

    class meta:
        ordering:("published",)

    def __str__(self):
        return "comment"






class Userprofile(models.Model):
    preffered_name = models.CharField(max_length=255,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic = CloudinaryField("userprofiles",default="userprofiles/dp.JPG")
    job_title = models.CharField(max_length=250,null=True)
    about = models.CharField(max_length=500,null=True)
    twitter = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)


    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('blog:existingprofile',kwargs={'pk': self.id})





