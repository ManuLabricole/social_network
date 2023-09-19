from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserProfile
# from friendship.models import Friendship

from .serializers import UserProfileSerializer, PublicProfileSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=['get'])
    # Because of the me function tge route is then users/me
    def me(self, request):
        userprofile = self.request.user.userprofile  # type: ignore
        serializer = self.get_serializer(userprofile)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     if not pk:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         user = UserProfile.objects.get(pk=pk)
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     # If the user is requesting their own profile
    #     if request.user == user:
    #         serializer = UserProfileSerializer(user)
    #     else:
    #         # Check if they are friends
    #         are_friends = Friendship.objects.filter(user1=request.user, user2=user).exists() or \
    #             Friendship.objects.filter(
    #                 user1=user, user2=request.user).exists()

    #         if are_friends:
    #             serializer = UserProfileSerializer(user)
    #         else:
    #             serializer = PublicProfileSerializer(user)

    #     return Response(serializer.data)
