from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from userprofile.models import UserProfile

from .models import Post, PostLike, Comment
from .serializers import PostSerializer


class FeedPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the user's profile
        user_profile = self.request.user.userprofile  # type: ignore

        # Get the user's friends
        friends = user_profile.friends.all()

        # Fetch posts authored by the user and their friends
        if friends:
            friends_posts = Post.objects.filter(author__in=friends)
            my_posts = Post.objects.filter(author=user_profile)

            # Convert querysets to lists and combine
            combined_posts = list(friends_posts) + list(my_posts)

            # Sort the combined list by 'created_at' in descending order
            sorted_posts = sorted(
                combined_posts, key=lambda x: x.created_at, reverse=True)

            return sorted_posts

        else:
            posts = Post.objects.all()
            return posts


class UserPostsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(author__user__id=user_id)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TogglePostLike(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=404)

        # Check if the user has already liked the post
        like = PostLike.objects.filter(
            post=post, user=request.user.userprofile).first()

        if like:
            # If a like exists, remove it (unlike the post)
            like.delete()
            return Response({"message": "Post unliked."})

        # If no like exists, create one (like the post)
        PostLike.objects.create(post=post, user=request.user.userprofile)
        return Response({"message": "Post liked."})
