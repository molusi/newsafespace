from django.urls import path
from . import views
from .views import userprofileview, UserProfileUpdateView, MyPostsView, articlecreateview, ArticleUpdateView, \
    ArticleDeleteView, ArticleDetailView, SearchView, comment_createview, upvote
from django.urls import path



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
    path('<int:pk>/detail/article', comment_createview, name='comment'),
    path('<int:pk>/commentdelete/',views.commentdelete,name='comment_delete'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='delete'),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('article/<int:article_id>/upvote/', views.upvote, name='article-upvote')
    ]


