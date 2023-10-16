from django.db.models.signals import post_save
from django.dispatch import receiver
from chat.models import Conversation, ConversationMessage


@receiver(post_save, sender=ConversationMessage)
def update_conversation_modified_at(sender, instance, **kwargs):
    conversation = instance.conversation
    conversation.save()  # This will update the modified_at field because of auto_now=True
