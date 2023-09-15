from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('', views.FriendRequestListView.as_view(),
         name='requests'),
    path('<str:request_id>/',
         views.UpdateFriendRequestStatusView.as_view(), name='update'),
    path('check-friendship/<uuid:profile_id>/',
         views.CheckFriendshipStatus.as_view(), name='check-friendship'),
]
