from django.http import JsonResponse
from django.views import View
from .models import UserProfile  # Import your UserProfile model here
# Create your views here.
# First we create View to handle the request to the endpoint /api/friendship/friend-request/
# We will use the POST method to create a new FriendRequest instance.


class SendFriendRequestView(View):
    def post(self, request, target_user_id):
        # user_profile = request.user.userprofile
        # target_user_profile = UserProfile.objects.get(id=target_user_id)

        # # Check if a friend request already exists
        # if target_user_profile in user_profile.friendship_requests.all():
        #     return JsonResponse({'message': 'Friend request already sent'})

        # user_profile.friendship_requests.add(target_user_profile)
        return JsonResponse({'message': 'Friend request sent'})
