from django.db import models
from django.contrib.auth.models import User

class Hall(models.Model):
    title = models.CharField(max_length=225)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Video(models.Model):
    title = models.CharField(max_length=225)
    url = models.URLField()
    youtube_id = models.CharField(max_length=225)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
