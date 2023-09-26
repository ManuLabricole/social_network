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
        validated_data['author'] = self.context['request'].user.userprofile
        return super().create(validated_data)
