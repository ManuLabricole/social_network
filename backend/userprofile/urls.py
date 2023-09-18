from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('me/', views.CurrentUserProfileView.as_view(), name='me'),
    path('posts/', include('post.urls')),
]
