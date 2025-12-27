from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = "user"
    CREATOR = "creator"

    ROLE_CHOICES = [
        (USER, "User"),
        (CREATOR, "Creator"),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=USER
    )

    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username


class Session(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sessions"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.session.title}"
