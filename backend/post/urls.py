from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('user/<uuid:user_id>/',
         views.UserSpecificPostsListView.as_view(), name='user-specific-posts-list'),
    path('me/', views.UserPostsListView.as_view(), name='user-posts'),

]
