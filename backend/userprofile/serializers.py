from rest_framework import serializers
from account.serializers import UserSerializer
from .models import UserProfile

from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = UserProfile
        # Add all fields you want
        fields = ['id', 'user', 'number_of_friends', 'friends']


class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']  # Only public fields
