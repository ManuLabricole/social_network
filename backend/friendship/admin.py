from django.contrib import admin
from .models import UserProfile

# We register the UserProfile model with the admin site.
admin.site.register(UserProfile)
