from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('send-request/', views.SendFriendRequestView.as_view(), name='send-request'),
]
