from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer


# List all conversations for the logged-in user
class ListConversationsView(generics.ListAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        return Conversation.objects.filter(user=self.request.user.userprofile)  # type: ignore


# Retrieve a single conversation along with its messages# Retrieve messages for a specific conversation
class RetrieveMessagesView(generics.ListAPIView):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.kwargs["conversation_id"]
        conversation = get_object_or_404(Conversation, id=conversation_id)
        return ConversationMessage.objects.filter(conversation=conversation)


# Create a new message in a conversation
class CreateMessageView(generics.CreateAPIView):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logic to associate the message with a conversation and the sender
        pass


# Delete a message from a conversation
class DeleteMessageView(generics.DestroyAPIView):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ConversationMessage.objects.filter(sender=self.request.user)
