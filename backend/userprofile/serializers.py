from rest_framework import serializers
from account.serializers import UserSerializer
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'friends']  # Add more fields if needed
