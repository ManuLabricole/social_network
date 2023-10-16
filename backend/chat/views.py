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
        messages = ConversationMessage.objects.filter(conversation=conversation)
        return messages


# Create a new message in a conversation
class CreateMessageView(generics.CreateAPIView):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        conversation = Conversation.objects.get(id=self.kwargs["conversation_id"])
        sender = self.request.user.userprofile

        # Assuming the conversation's user field is a ManyToManyField with UserProfiles
        users = conversation.user.all()
        receiver = next(user for user in users if user != sender)

        serializer.save(
            sender=sender,
            receiver=receiver,
            conversation=conversation,
        )


# Delete a message from a conversation
class DeleteMessageView(generics.DestroyAPIView):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ConversationMessage.objects.filter(sender=self.request.user)
