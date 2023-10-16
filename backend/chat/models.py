from django.db import models
from userprofile.models import UserProfile


# Create your models here.
class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(UserProfile, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["modified_at"]

    def __str__(self):
        return f"Conversation {self.id}"


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        UserProfile, related_name="sent_messages", on_delete=models.SET_NULL, null=True
    )
    receiver = models.ForeignKey(
        UserProfile,
        related_name="received_messages",
        on_delete=models.SET_NULL,
        null=True,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
