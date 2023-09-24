import uuid
from django.db import models
from account.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    number_of_friends = models.IntegerField(default=0)

    def __str__(self):
        return f"UserProfile - {self.user.email}"

    def remove_friend(self, friend_profile):
        """Remove a friend from both user's and friend's lists."""
        self.friends.remove(friend_profile)
        friend_profile.friends.remove(self)
