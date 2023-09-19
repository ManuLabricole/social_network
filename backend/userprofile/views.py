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

    def retrieve(self, request, pk=None):

        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            userprofile = UserProfile.objects.get(user__id=pk)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(userprofile)
        print(request.user)

        # If the user is requesting their own profile
        if request.user == userprofile.user:
            serializer = UserProfileSerializer()
        else:
            # Check if they are friends
            if request.user.userprofile in userprofile.friends.all():
                print("They are friends")
                serializer = UserProfileSerializer(userprofile)
            else:
                print("They are not friends")
                serializer = PublicProfileSerializer(userprofile)

        return Response(serializer.data)
