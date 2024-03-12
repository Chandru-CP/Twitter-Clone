from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default=False)
    profile_picture = models.ImageField(upload_to='images/', default='images/default.jpeg')

    def __str__(self):
        return self.user.email
