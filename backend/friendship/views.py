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

    def get_queryset(self):
        print(self.request.query_params) # type: ignore
        request_type = self.request.query_params.get( # type: ignore
            'request_type', 'pending')
        user_profile = self.request.user.userprofile  # type: ignore

        if request_type == 'pending':
            return FriendRequest.objects.filter(receiver=user_profile, status='PENDING')
        elif request_type == 'accepted':
            return FriendRequest.objects.filter(receiver=user_profile, status='ACCEPTED')
        else:
             # Default to returning pending requests or handle other cases
            return FriendRequest.objects.filter(receiver=user_profile, status='PENDING')
