from django.contrib import admin
from .models import UserProfile, FriendRequest

# We register the UserProfile model with the admin site.
admin.site.register(UserProfile)
admin.site.register(FriendRequest)
