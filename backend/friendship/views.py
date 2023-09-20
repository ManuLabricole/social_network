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
