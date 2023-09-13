from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer

from .forms import PostForm

# Here we render the list of posts


class PostListView(generics.ListCreateAPIView):
    print("PostListView")
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        print("Inside create method")
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return JsonResponse(serializer.data, status=201)

        else:
            print(serializer.errors)
            response = JsonResponse(serializer.errors, status=400)
            return response


class UserPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
