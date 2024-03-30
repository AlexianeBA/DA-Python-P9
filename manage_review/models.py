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
    title = models.CharField(max_length=128, default="")
    content = models.TextField(max_length=2048, default="")
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def formatted_created_at(self):
        return self.created_at.strftime("%d-%m-%Y à %H:%M:%S")

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=128, default="")
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField(
        
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128)
    commentary = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="images/", default="")
    content = models.TextField(max_length=2048, default="")
    title = models.CharField(max_length=128, default="")

    def formatted_created_at(self):
        return self.time_created.strftime("%d-%m-%Y à %H:%M:%S")
