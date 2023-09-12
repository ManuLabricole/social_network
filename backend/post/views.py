from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer

from .forms import PostForm


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def post_create(request):
    print(request.data)
    print(request.user)
    form = PostForm(request.data)
    if form.is_valid():
        post = form.save(commit=False)  # commit=False means that we don't want to save the form to the database yet
        post.author = request.user
        post.save()
        
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
        
    else:
        return JsonResponse({'status': 'error'})

    return JsonResponse({'status': 'ok'})
