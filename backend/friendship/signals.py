from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from account.models import User
from .models import FriendRequest
# from .models import UserProfile


@receiver(post_save, sender=FriendRequest)
def update_friends_on_accept(sender, instance, **kwargs):
    if instance.status == 'ACCEPTED':
        instance.sender.friends.add(instance.receiver)
        instance.receiver.friends.add(instance.sender)


@receiver(post_save, sender=FriendRequest)
def remove_friends_on_decline(sender, instance, **kwargs):
    if instance.status == 'DECLINED':
        instance.sender.friends.remove(instance.receiver)
        instance.receiver.friends.remove(instance.sender)


@receiver(post_delete, sender=FriendRequest)
def remove_friends_on_delete(sender, instance, **kwargs):
    instance.sender.friends.remove(instance.receiver)
    instance.receiver.friends.remove(instance.sender)
