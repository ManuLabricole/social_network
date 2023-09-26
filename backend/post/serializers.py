from rest_framework import serializers
from .models import Post, PostAttachment
from userprofile.serializers import UserProfileSerializer


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'image', 'created_by')


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',
                  'created_at_formatted', 'attachment')

    def create(self, validated_data):
        # Set the author to the current user's profile
        user_profile = self.context['request'].user.userprofile
        post = Post.objects.create(author=user_profile, **validated_data)
        return post
