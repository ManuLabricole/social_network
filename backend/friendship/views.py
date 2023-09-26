from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from userprofile.models import UserProfile
from .models import FriendRequest
from .serializers import FriendRequestSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pending_friend_requests(request):
    pending_requests = FriendRequest.objects.filter(
        receiver=request.user.userprofile, status='PENDING')

    # for request in requests:
    #     print('SENDER :', request.sender)
    #     print('RECEIVER :', request.receiver)
    #     print('STATUS :', request.status)
    # print(pending_requests)
    serializer = FriendRequestSerializer(pending_requests, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def friendship(request, friend_id):
    user_profile = request.user.userprofile
    try:
        friend_profile = UserProfile.objects.get(id=friend_id)
    except UserProfile.DoesNotExist:
        return Response({"error": "Friend not found."}, status=404)

    if friend_profile not in user_profile.friends.all():
        return Response({"error": "This user is not your friend."}, status=400)

    user_profile.remove_friend(friend_profile)
    return Response({"message": "Friend removed successfully."})


class FriendshipView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, friend_id):
        user_profile = request.user.userprofile
        friend_profile = UserProfile.objects.get(user__id=friend_id)
        print("FRIEND_ID", friend_id)
        print("USER_ID", user_profile.user.id)

        friend_request_sent = FriendRequest.objects.filter(
            sender=user_profile, receiver=friend_profile).first()
        friend_request_received = FriendRequest.objects.filter(
            sender=friend_profile, receiver=user_profile).first()

        if friend_request_sent:
            return Response({
                "message": "Friend request sent.",
                "request": "SENT",
                "status": friend_request_sent.status
            })
        if friend_request_received:
            return Response({
                "message": "Friend request received.",
                "request": "RECEIVED",
                "status": friend_request_received.status,
            })
        else:
            return Response({
                "message": "No friend request sent or received.",
                "request": None,
                "status": None
            })

    def post(self, request, friend_id):
        user_profile = request.user.userprofile
        friend_profile = UserProfile.objects.get(user__id=friend_id)

        if friend_profile in user_profile.friends.all():
            return Response({"error": "This user is already your friend."}, status=400)

        if FriendRequest.objects.filter(sender=user_profile, receiver=friend_profile).exists():
            return Response({"error": "Friend request already sent."}, status=400)

        if FriendRequest.objects.filter(sender=friend_profile, receiver=user_profile).exists():
            request = FriendRequest.objects.filter(
                sender=friend_profile, receiver=user_profile).last()
            if request.status == 'ACCEPTED': # type: ignore
                return Response({"error": "You are already friends with this user."}, status=400)
                return Response({"error": "You already have a friend request from this user."}, status=400)
            elif request.status == 'DECLINED': # type: ignore
                request.delete() # type: ignore
                friend_request = FriendRequest(
                    sender=user_profile, receiver=friend_profile)
                friend_request.save()
                return Response({"message": "Friend request sent."})

        friend_request = FriendRequest(
            sender=user_profile, receiver=friend_profile)
        friend_request.save()
        return Response({"message": "Friend request sent."})
    
    def put(self, request, friend_id):
        friend = UserProfile.objects.get(user__id=friend_id)
        try:
            friend_request = FriendRequest.objects.get(
                sender=friend, receiver=request.user.userprofile)

        except FriendRequest.DoesNotExist:
            return Response({"error": "Request not found."}, status=404)

        print('Friend_request status', friend_request.status)
        print('data', request.data["status"])

        if 'status' in request.data:
            if request.data['status'] == 'ACCEPTED':
                print("yes")
                # Add each other to friends list and update the number of friends
                request.user.userprofile.friends.add(
                    friend_request.sender)
                friend_request.sender.friends.add(
                    request.user.userprofile)
                friend_request.status = 'ACCEPTED'
                friend_request.save()
                return Response({"message": "Friend request accepted."})

            elif request.data['status'] == 'DECLINED':
                friend_request.status = 'DECLINED'
                friend_request.save()
                return Response({"message": "Friend request rejected."})

        return Response({
            "error": "Invalid action.",
            "message": f"{request.data['status']} : is a not valid input. Only ACCEPTED or DECLINED is valid."
        }, status=400)

    def delete(self, request, friend_id):
        user_profile = request.user.userprofile
        friend_profile = UserProfile.objects.get(user__id=friend_id)

        if friend_profile not in user_profile.friends.all():
            return Response({"error": "This user is not your friend."}, status=status.HTTP_400_BAD_REQUEST)

        request = FriendRequest.objects.filter(
            sender=user_profile, receiver=friend_profile).first()

        if request is None:
            request = FriendRequest.objects.filter(
                sender=friend_profile, receiver=user_profile).first()

        try:
            request.delete()  # type: ignore
            return Response({"message": "Friend removed successfully."})
        except:
            return Response({"error": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)

