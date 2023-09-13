from rest_framework import serializers
from .models import Post, PostAttachment
from account.serializers import UserSerializer


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'image', 'created_by')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at', 'attachment')
