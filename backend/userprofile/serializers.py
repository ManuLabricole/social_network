from rest_framework import serializers
from account.serializers import UserSerializer
from .models import UserProfile

from rest_framework import serializers


class SimpleUserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserProfile
        # Add all fields you want
        fields = ['id', 'user', 'number_of_friends', 'friends']


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    friends = SimpleUserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        # Add all fields you want
        fields = ['id', 'user', 'number_of_friends', 'friends']


class PublicProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user']
