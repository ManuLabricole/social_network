from django.urls import path
from . import views

urlpatterns = [
    path('me/pending/', views.pending_friend_requests,
         name='pending-friend-requests'),
    path('requests/<uuid:friend_id>/', views.FriendshipView.as_view(),
         name='update-friend-requests'),
]
