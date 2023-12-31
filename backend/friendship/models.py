import uuid
from django.db import models
from userprofile.models import UserProfile


class FriendRequest(models.Model):
    class Meta:
        unique_together = ['sender', 'receiver']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='friend_request_sender')

    receiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='friend_request_receiver')

    STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('ACCEPTED', 'accepted'),
        ('DECLINED', 'declined'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"sender - {self.sender.user.email} / receiver - {self.receiver.user.email}"
