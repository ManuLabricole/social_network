from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.FeedPostsListView.as_view(), name='feed-posts-list'),
    path('',
         views.UserPostsListView.as_view(), name='user-posts-list'),

]
