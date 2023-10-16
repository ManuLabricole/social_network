from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, CreateMessageSerializer


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
class CreateMessageView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, conversation_id, *args, **kwargs):
        # Find the conversation
        conversation = get_object_or_404(Conversation, id=conversation_id)

        # Identify the sender and receiver
        sender = request.user.userprofile
        users = conversation.user.all()
        receiver = next(user for user in users if user != sender)

        # Get the body from the request data
        body = request.data.get("body", "")

        # Prepare the data
        data = {
            "sender": sender.id,
            "receiver": receiver.id,
            "conversation": conversation.id,
            "body": body,
        }

        # Serialize the data
        serializer = CreateMessageSerializer(data=data)

        # Validate and save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a message from a conversation
class DeleteMessageView(generics.DestroyAPIView):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ConversationMessage.objects.filter(sender=self.request.user)
