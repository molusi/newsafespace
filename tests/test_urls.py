import unittest
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import bloghome, person_login, MyPostsView, UserProfileUpdateView, existinguserprofile, SearchView, \
    articlecreateview \
 \
 \
#
# path('userprofile/', userprofileview, name='userprofile_create'),
# path('<int:pk>/updateuserprofile/', UserProfileUpdateView.as_view(), name='userprofile_update'),
# path('<int:pk>/existingprofile/', views.existinguserprofile, name='existingprofile'),
# path('create/', views.articlecreateview, name='article-create'),
# path('myposts/', MyPostsView.as_view(), name='myposts'),
# path('search/', SearchView.as_view(), name="search"),
# path('<int:pk>/detail/', ArticleDetailView.as_view(), name='detail'),
# path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),
# path('<int:pk>/detail/article', comment_createview, name='comment'),
# path('<int:pk>/commentdelete/', views.commentdelete, name='comment_delete'),
# path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
# path('activate/<uidb64>/<token>', views.activate, name="activate"),
# path('article/<int:article_id>/upvote/', views.upvote, name='article-upvote')
class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url=reverse('blog:home')
        self.assertEqual(resolve(url).func,bloghome)

    def test_create_url_resolves(self):
        url = reverse('blog:article-create')
        self.assertEqual(resolve(url).func, articlecreateview)
    def test_search_url_resolves(self):
        url=reverse('blog:search')
        self.assertEqual(resolve(url).func.view_class,SearchView)

    def test_myposts_url_resolves(self):
        url=reverse('blog:myposts')
        self.assertEqual(resolve(url).func.view_class,MyPostsView)

    # def test_userprofile_create(self):
    #     url=reverse('blog:userprofile_create')
    #     self.assertEqual(resolve(url).func,UserProfileUpdateView.as_view())
    #
    # def test_existing_profile(self):
    #     url=reverse('blog:existingprofile')
    #     self.assertEqual(resolve(url).func,existinguserprofile())








# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
