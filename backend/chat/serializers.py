from datetime import timedelta
from django.utils import timezone

from rest_framework import serializers
from .models import Conversation, ConversationMessage
from userprofile.serializers import SimpleUserProfileSerializer


class ConversationSerializer(serializers.ModelSerializer):
    user = SimpleUserProfileSerializer(many=True)  # Include user details
    modified_at_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ("id", "user", "created_at", "modified_at", "modified_at_formatted")

    def get_modified_at_formatted(self, obj):
        now = timezone.now()  # Make it timezone-aware
        modified_at = obj.modified_at
        delta = now - modified_at
        
        if delta < timedelta(minutes=1):
            return "now"

        elif delta < timedelta(minutes=60):
            return f"{delta.seconds // 60} minutes ago"
        elif delta < timedelta(hours=24):
            return f"{delta.seconds // 3600} hours ago"
        elif delta < timedelta(days=30):
            return f"{delta.days} days ago"
        elif delta < timedelta(days=365):
            return f"{delta.days // 30} months ago"
        else:
            years = delta.days // 365
            months = (delta.days % 365) // 30
            return f"{years} years, {months} months ago"


class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = "__all__"
