from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    print(queryset)
