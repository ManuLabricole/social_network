# Generated by Django 4.2.5 on 2023-10-15 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userprofile", "0002_userprofile_number_of_friends"),
        ("chat", "0004_alter_conversation_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="user",
            field=models.ManyToManyField(
                related_name="conversations", to="userprofile.userprofile"
            ),
        ),
        migrations.AlterField(
            model_name="conversationmessage",
            name="receiver",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="received_messages",
                to="userprofile.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="conversationmessage",
            name="sender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sent_messages",
                to="userprofile.userprofile",
            ),
        ),
    ]
