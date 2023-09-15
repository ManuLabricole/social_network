import uuid
from django.db import models
from account.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    friendship_requests = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"UserProfile - {self.user.email}"


class FriendRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='friend_request_sender')
    receiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='friend_request_receiver')
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
