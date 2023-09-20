from django.urls import path
from . import views

urlpatterns = [
    path('pending/', views.pending_friend_requests, name='pending-friend-requests'),
]
