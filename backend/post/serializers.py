from rest_framework import serializers
from .models import Post, PostAttachment, PostLike, Comment
from userprofile.serializers import UserProfileSerializer


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'image', 'created_by')


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    isLike = serializers.SerializerMethodField()

    likes = PostLikeSerializer(
        source='postlike_set', many=True, read_only=True)
    comments = CommentSerializer(
        source='comment_set', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',
                  'created_at_formatted', 'attachment', 'likes', 'comments', 'isLike')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.userprofile
        return super().create(validated_data)

    def get_isLike(self, obj):
        user_profile = self.context['request'].user.userprofile
        return PostLike.objects.filter(post=obj, user=user_profile).exists()
