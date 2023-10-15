from rest_framework import serializers
from .models import Conversation, ConversationMessage
from userprofile.serializers import SimpleUserProfileSerializer


class ConversationSerializer(serializers.ModelSerializer):
    user = SimpleUserProfileSerializer(many=True)  # Include user details

    class Meta:
        model = Conversation
        fields = ("id", "user", "created_at", "modified_at")


class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = "__all__"
