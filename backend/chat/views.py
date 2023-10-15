from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer


# List all conversations for the logged-in user
class ListConversationsView(generics.ListAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)


# Retrieve a single conversation along with its messages
class RetrieveConversationView(generics.RetrieveAPIView):
    serializer_class = ConversationSerializer  # You might need a different serializer to include messages
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)


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
