import uuid
from django.db import models
from django.utils.timesince import timesince

from userprofile.models import UserProfile

# Model for storing post attachments, such as images.


class PostAttachment(models.Model):
    def __str__(self):
        return str(self.id)
    # Unique identifier for each attachment.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Image file associated with the attachment (can be null or blank).
    image = models.ImageField(
        upload_to='post_attachments', blank=True, null=True)

    # The user who created this attachment.
    created_by = models.ForeignKey(
        UserProfile, related_name='post_attachments', on_delete=models.CASCADE)

# Model for representing posts made by users.


class Post(models.Model):
    def __str__(self):
        return f"{self.title} by {self.author}"
    # Unique identifier for each post.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # The author of the post.
    author = models.ForeignKey(
        UserProfile, related_name='posts', on_delete=models.CASCADE)

    # The title of the post (limited to 50 characters).
    title = models.CharField(max_length=50)

    # The main content or body of the post.
    body = models.TextField()

    # The date and time when the post was created (auto-generated).
    created_at = models.DateTimeField(auto_now_add=True)

    # Many-to-many relationship with PostAttachment for including attachments with the post.
    attachment = models.ManyToManyField(
        PostAttachment, related_name='post_attachments', blank=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def created_at_formatted(self):
        return timesince(self.created_at)
    # To be added in the future:
    # - Likes: To track users who liked this post.
    # - Likes count: To count the number of likes on this post.


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']


class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
