from django.db import models
from django_accounts.models import CustomUser
from datetime import datetime
from django_profile.models import UserProfile


class Hashtag(models.Model):
    hashtags = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtags


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', default='images/default.jpeg')
    message = models.CharField(max_length=100)
    hashtags = models.ManyToManyField(Hashtag)
    timestamp = models.DateTimeField(auto_now_add=True)
    num_likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comment)
    current_timestamp = datetime.now()

    def __str__(self):
        return self.message


