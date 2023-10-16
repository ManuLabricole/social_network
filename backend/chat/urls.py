from django.urls import path
from . import views

urlpatterns = [
    path("me/", views.ListConversationsView.as_view(), name="conversation-list"),
    path(
        "<int:conversation_id>/",
        views.RetrieveMessagesView.as_view(),
        name="retrieve_messages",
    ),
    path(
        "<int:conversation_id>/messages/",
        views.CreateMessageView.as_view(),
        name="create_message",
    ),
]
