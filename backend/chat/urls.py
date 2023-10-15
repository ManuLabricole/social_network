from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListConversationsView.as_view(), name="conversation-list"),
]
