import unittest
from django.test import TestCase,Client
from blog.models import Article,Comment,Userprofile,Vote
from django.urls import reverse
import json

from blog.views import bloghome

csrf_client = Client(enforce_csrf_checks=True)
# class TestMyViews(TestCase):

    # def test_blog_home_view_get(self):
    #     client = Client()
    #     response=client.get(reverse('blog:home'))
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,'/templates/accounts/person_login.html')


if __name__ == '__main__':
    unittest.main()
