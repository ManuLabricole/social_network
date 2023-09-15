from django.http import JsonResponse
from django.views import View
from .models import UserProfile  # Import your UserProfile model here
# Create your views here.
# First we create View to handle the request to the endpoint /api/friendship/friend-request/
# We will use the POST method to create a new FriendRequest instance.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from .models import FriendRequest
from .serializers import FriendRequestSerializer


class FriendRequestListView(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = FriendRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Customize the serializer to set the sender as the current user
            serializer.validated_data['sender'] = self.request.user.userprofile
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            response = JsonResponse(serializer.errors, status=400)
            return response

    def get_queryset(self):
        user_profile = self.request.user.userprofile
        queryset = user_profile.friendship_requests.all()
        return queryset
