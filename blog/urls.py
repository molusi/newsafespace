from django.urls import path
from . import views
from .views import userprofileview,UserProfileUpdateView, MyPostsView, articlecreateview,ArticleUpdateView, ArticleDeleteView, ArticleDetailView, SearchView
from django.urls import path
from . models import Userprofile


app_name = "blog"

urlpatterns = [
    path('',views.bloghome,name='home'),
    path('userprofile/',userprofileview,name='userprofile_create'),
    path('<int:pk>/updateuserprofile/',UserProfileUpdateView.as_view(),name='userprofile_update'),
    path('<int:pk>/existingprofile/',views.existinguserprofile, name='existingprofile'),
    path('create/',views.articlecreateview, name='article-create'),
    path('myposts/', MyPostsView.as_view(), name='myposts'),
    path('search/',SearchView.as_view(),name="search"),
    path('<int:pk>/detail/',ArticleDetailView.as_view(),name='detail'),
    path('<int:pk>/update/',ArticleUpdateView.as_view(),name='update'),
    path('<int:pk>/commentupdate/',views.commentupdate,name='comment_update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='delete'),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    ]


