from rest_framework import serializers
from .models import FriendRequest, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user']  # Add more fields if needed


class FriendRequestSerializer(serializers.ModelSerializer):
    sender = UserProfileSerializer()
    receiver = UserProfileSerializer()

    class Meta:
        model = FriendRequest
        fields = ['id', 'status', 'created_at', 'sender', 'receiver']
