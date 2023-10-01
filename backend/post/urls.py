from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.FeedPostsListView.as_view(), name='feed-posts-list'),
    path('',
         views.UserPostsView.as_view(), name='user-posts-list'),
    path('<uuid:pk>/like', views.PostLikeView.as_view(), name='post-detail'),
    path('<uuid:pk>/comment', views.CreateCommentView.as_view(), name='post-detail'),
]
