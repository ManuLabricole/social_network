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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(Post.objects.filter(author=self.request.user))
        return Post.objects.filter(author=self.request.user)


class UserSpecificPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        print("All kwargs:", self.kwargs)
        user_id = self.kwargs.get('user_id', None)

        print("Type of user_id:", type(user_id))
        print("Request data:", self.request)
        print("Request headers:", self.request.headers)

        if user_id:
            result = Post.objects.filter(author__id=user_id)
            print("Query result:", result)
            return result
        else:
            return Post.objects.all()
