# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from LITRevu.settings import STATIC_URL


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="uploaded_tickets", null=True
    )
    title = models.CharField(max_length=200, default="")
    content = models.TextField(default="")
    image = models.ImageField(upload_to=STATIC_URL + "/images/", default="")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
