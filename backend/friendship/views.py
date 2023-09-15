from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views import View
from .models import UserProfile  # Import your UserProfile model here
# Create your views here.
# First we create View to handle the request to the endpoint /api/friendship/friend-request/
# We will use the POST method to create a new FriendRequest instance.

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


from .models import FriendRequest
from .serializers import FriendRequestSerializer


class FriendRequestListView(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        sender = request.user.userprofile
        receiver_id = request.data.get('receiver')
        receiver = UserProfile.objects.get(id=receiver_id)

        # Check if a friend request already exists
        existing_request = FriendRequest.objects.filter(
            sender=sender, receiver=receiver)
        if existing_request.exists():
            return JsonResponse({'error': 'Friend request already sent.'}, status=400)
        # If no existing request, create a new one
        friend_request = FriendRequest(sender=sender, receiver=receiver)
        friend_request.save()
        serializer = self.get_serializer(friend_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):  # type: ignore
        request_type = self.request.query_params.get(  # type: ignore
            'request_type')

        user_profile = self.request.user.userprofile  # type: ignore

        if request_type == 'pending':
            return FriendRequest.objects.filter(receiver=user_profile, status='PENDING')

        elif request_type == 'accepted':
            return FriendRequest.objects.filter(receiver=user_profile, status='ACCEPTED')

        elif request_type == 'declined':
            # Default to returning pending requests or handle other cases
            return FriendRequest.objects.filter(receiver=user_profile, status='PENDING')

        else:
            raise ValidationError({"error": "Invalid request_type provided."})


class UpdateFriendRequestStatusView(APIView):
    permission_classes = [IsAuthenticated]
    print("hello")

    def put(self, request, request_id):
        # print(request.data)
        # print(request_id)
        # print(**kwargs)

        new_status = request.data.get('status')

        try:
            friend_request = FriendRequest.objects.get(id=request_id)
            print(friend_request)
        except FriendRequest.DoesNotExist:
            return Response({'error': 'Friend request not found.'}, status=status.HTTP_404_NOT_FOUND)

        if new_status not in ['ACCEPTED', 'DECLINED']:
            return Response({'error': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        friend_request.status = new_status
        friend_request.save()

        return Response({'message': 'Status updated successfully.'}, status=status.HTTP_200_OK)


class CheckFriendshipStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, profile_id):
        print(request.data)
        print(profile_id)
        return Response({'message': 'Not friends'}, status=status.HTTP_200_OK)
        user_profile = self.request.user.userprofile  # type: ignore
        friend_id = self.request.query_params.get('friend_id')  # type: ignore
        friend_profile = UserProfile.objects.get(id=friend_id)

        if friend_profile in user_profile.friends.all():
            return Response({'message': 'Friends'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not friends'}, status=status.HTTP_200_OK)
