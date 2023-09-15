# myapp/management/commands/create_user_profiles.py
from django.core.management.base import BaseCommand
from friendship.models import User, UserProfile


class Command(BaseCommand):
    help = 'Create UserProfile instances for existing users'

    def handle(self, *args, **options):
        users_without_profile = User.objects.filter(userprofile__isnull=True)

        for user in users_without_profile:
            UserProfile.objects.create(user=user)

        self.stdout.write(self.style.SUCCESS(
            'UserProfiles created successfully.'))
