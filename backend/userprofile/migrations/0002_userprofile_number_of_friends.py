# Generated by Django 4.2.5 on 2023-09-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='number_of_friends',
            field=models.IntegerField(default=0),
        ),
    ]
