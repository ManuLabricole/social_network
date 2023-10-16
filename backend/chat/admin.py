from django.contrib import admin
from .models import Conversation, ConversationMessage


# Register Conversation model
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "modified_at")
    search_fields = ("id",)
    list_filter = ("created_at", "modified_at")


# Register ConversationMessage model
@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "conversation",
        "sender",
        "receiver",
        "body",
        "created_at",
        "modified_at",
    )
    search_fields = ("text", "sender__username")
    list_filter = ("created_at", "modified_at")
