from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    album = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    release_date = models.DateField()