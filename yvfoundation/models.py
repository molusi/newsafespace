from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

TOPIC_CHOICES = (
 ('general', 'General enquiry'),
 ('bug', 'Bug report'),
 ('suggestion', 'Suggestion'),
)

class Contact(models.Model):
    topic = models.CharField(choices=TOPIC_CHOICES,max_length=40)
    message = models.CharField(max_length=200)
    sender = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.topic