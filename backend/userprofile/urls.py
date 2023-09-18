from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.CurrentUserProfileView.as_view(), name='me'),
]
