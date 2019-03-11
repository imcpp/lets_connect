from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#User = get_user_model()
class User(AbstractUser):
    enroll_no = models.CharField(max_length=12, unique=True)
    bio = models.CharField(max_length=200, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username


class Room(models.Model):
    room_name=models.CharField(max_length=128)
    def __str__(self):
        return self.room_name

class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author_messages', on_delete=models.CASCADE)
    author1=models.ForeignKey(Room,related_name="message1",on_delete=models.CASCADE,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    poet = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text
