from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


class FeedPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the user's profile
        # user_profile = self.request.user.userprofile
        # # Get the user's friends
        # friends = user_profile.friends.all()
        # # Fetch posts authored by the user and their friends
        # return Post.objects.filter(author__in=friends).union(
        #     Post.objects.filter(author=user_profile)
        # ).order_by('-created_at')
        return Post.objects.all().order_by('-created_at')
