from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('me/', views.UserPostsListView.as_view(), name='user-posts'),

]
