from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db.models import Q

from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # Here we rewrite the create method to add the author to the post
    def create(self, request):

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return JsonResponse(serializer.data, status=201)

        else:
            print(serializer.errors)
            response = JsonResponse(serializer.errors, status=400)
            return response

    # Here we rewrite the get method to filter if needed
    def get_queryset(self):
        # Start with all posts
        queryset = Post.objects.all()

        # Filter by search query if provided
        search_query = self.request.query_params.get(  # type: ignore
            'search', None)
        print("Search query:", search_query)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query) |
                # Assuming you have a username field in your user model
                Q(author__username__icontains=search_query)
            )

        # Filter by user_id if provided
        user_id = self.kwargs.get('user_id', None)
        if user_id:
            queryset = queryset.filter(author__id=user_id)

        return queryset


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
