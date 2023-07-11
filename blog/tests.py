from django.test import TestCase
import datetime
from django.urls import reverse
from django.utils import timezone
from blog.models import Article,Userprofile,User



class BloghomeViewTests(TestCase):
    def test_articles(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['articles'], [])




