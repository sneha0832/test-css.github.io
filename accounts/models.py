from django.db import models
from django.contrib.auth.models import User

from personal_portfolio import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"


class Child(models.Model):
    GENDER_CHOICES = (
        ('boy', 'Boy'),
        ('girl', 'Girl'),
        ('not_say', 'Prefer not to say'),
    )
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='not_say')

    class Meta:
        db_table = 'accounts_child'

    def __str__(self):
        return self.name


class ChatbotResponse(models.Model):
    trigger = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.trigger


# model that stores the time spent by each user on different pages
"""""""""""
class PageTimeSpent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.CharField(max_length=2048)
    time_spent = models.IntegerField(help_text="Time spent in milliseconds")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} spent {self.time_spent} on {self.url}"
        """""""""