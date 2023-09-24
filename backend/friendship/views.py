from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_friend_request(request, request_id):
    print(request.data)
    try:
        friend_request = FriendRequest.objects.get(
            id=request_id, receiver=request.user.userprofile)
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
            friend_request.status = 'rejected'
            # friend_request.save()
            return Response({"message": "Friend request rejected."})

    return Response({"error": "Invalid action."}, status=400)
