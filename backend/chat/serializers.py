from rest_framework import serializers
from .models import Conversation, ConversationMessage
from userprofile.serializers import UserProfileSerializer


class ConversationSerializer(serializers.ModelSerializer):
    other_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Conversation
        fields = ("id", "other_user", "created_at", "modified_at")


class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = "__all__"
