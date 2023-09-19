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
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user_name']

    def get_user_name(self, obj):
        return obj.user.name
