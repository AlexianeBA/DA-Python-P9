from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserFollows(models.Model):
    user = models.ForeignKey(
        to=User, related_name="following", on_delete=models.CASCADE
    )
    followed_user = models.ForeignKey(
        to=User, related_name="followers", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            "user",
            "followed_user",
        )

    def __str__(self):
        return f"{self.user} suit {self.followed_user}"
