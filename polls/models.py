from django.db import models
from blog.storage_backends import PublicMediaStorage


# Create your models here.
class Blog(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    date = models.CharField(max_length=200)
    urlCTA = models.CharField(max_length=200)
    imgPost = models.FileField(storage=PublicMediaStorage(), default='/blogger/cargo-ship.png')