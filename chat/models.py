from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Room(models.Model):
    room_name=models.CharField(max_length=128)
    def __str__(self):
        return self.room_name

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    author1=models.ForeignKey(Room,related_name="message1",on_delete=models.CASCADE,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    poet = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text
