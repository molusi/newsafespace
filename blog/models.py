from urllib.request import urlopen

import cloudinary
import tinify
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.core.files.uploadedfile import InMemoryUploadedFile

import accounts.models
from accounts.models import User
user = get_user_model()



class Article(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('blog_image',default="https://res.cloudinary.com/abimolusi/image/upload/v1690459183/pen-paper-tea-go_n9dgcg.webp")
    content = models.TextField()
    author = models.ForeignKey("Userprofile",on_delete=models.SET_NULL,blank=True,null=True)
    created = models.DateField(auto_now_add=True)
    comments_all = models.ManyToManyField("Comment", blank=True,related_name='thecomments')
    votes=models.ManyToManyField("Vote",null=True,related_name='thevotes')

    def save(self, *args, **kwargs):
        # Check if the profilepic field has changed
        if self.pk is not None:
            try:
                old_article = Article.objects.get(pk=self.pk)
                if self.image!= old_article.image:
                    # Read the image data from the InMemoryUploadedFile object
                    if isinstance(self.image, InMemoryUploadedFile):
                        image_data = self.image.read()

                        # Compress the image with Tinify
                        tinify.key = "TxkRT8fyVQJ0cLcn1X4KB3r7d6M8bM9T"
                        source = tinify.from_buffer(image_data)
                        compressed_image = source.to_buffer()

                        # Upload the compressed image to Cloudinary
                        cloudinary_response = cloudinary.uploader.upload(compressed_image)

                        # Update the profilepic field with the new Cloudinary URL
                        self.image = cloudinary_response["secure_url"]
            except Article.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk': self.id})

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    upvote = models.IntegerField(default=1)



class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    author = models.ForeignKey("Userprofile",on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    hide = models.BooleanField(default=False)

    class meta:
        ordering:("published",)

    def __str__(self):
        return self.content

    import tinify
    from django.db import models
    from cloudinary.models import CloudinaryField

class Userprofile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=255, null=False)
    profilepic = CloudinaryField("userprofiles", default="https://res.cloudinary.com/abimolusi/image/upload/v1690024654/person_lgnirh.jpg")
    about = models.CharField(max_length=500, null=True)
    linkedin = models.URLField(blank=True, null=True,default='https://www.linkedin.com/in/abigail-molusi-a8719b229/?originalSubdomain=za')


    from urllib.request import urlopen

    def save(self, *args, **kwargs):
        # Check if the profilepic field has changed
        if self.pk is not None:
            try:
                old_profile = Userprofile.objects.get(pk=self.pk)
                if self.profilepic != old_profile.profilepic:
                    # Read the image data from the InMemoryUploadedFile object
                    if isinstance(self.profilepic, InMemoryUploadedFile):
                        image_data = self.profilepic.read()

                        # Compress the image with Tinify
                        tinify.key = "TxkRT8fyVQJ0cLcn1X4KB3r7d6M8bM9T"
                        source = tinify.from_buffer(image_data)
                        compressed_image = source.to_buffer()

                        # Upload the compressed image to Cloudinary
                        cloudinary_response = cloudinary.uploader.upload(compressed_image)

                        # Update the profilepic field with the new Cloudinary URL
                        self.profilepic = cloudinary_response["secure_url"]
            except Userprofile.DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def __str__(self):
        return self.preferred_name

    def get_absolute_url(self):
        return reverse('blog:existingprofile',kwargs={'pk': self.user.id})





