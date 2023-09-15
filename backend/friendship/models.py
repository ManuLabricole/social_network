from django.db import models
from account.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    friendship_requests = models.ManyToManyField('self', blank=True)

    def __str__(self) -> str:
        return super().__str__()
