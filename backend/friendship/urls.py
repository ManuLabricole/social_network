from django.urls import path
from . import views

urlpatterns = [
    path('pending/', views.pending_friend_requests,
         name='pending-friend-requests'),
    path('<uuid:request_id>/', views.update_friend_request,
         name='update-friend-requests'),
]
